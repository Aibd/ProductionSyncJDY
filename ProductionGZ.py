from MSSqlDB import MSSqlDBManager
from SQLiteDB import SqliteDBManager
from jdy import JDYApi
from logger import Logger
from common import Common
import utils


# 简道云批量删除数据
def delete_jdy_data(jdy_api, kdata):
    query_data = Common.query_data
    billno = kdata[0][1]
    company = kdata[0][-1]
    query_data["filter"]["cond"][0]["value"] = billno
    query_data["filter"]["cond"][1]["value"] = company
    id = jdy_api.query_dataid(query_data)
    if id:
        jdy_api.batch_delete(entry_id=Common.entry_id, ids=id)


# Sqlite批量删除数据
def delete_sqlite_data(dbname, tablename, kdata):
    with SqliteDBManager(dbname) as sqlitemanager:
        billno = kdata[0][1]
        company = kdata[0][-1]
        sqlitemanager.execute(
            f"DELETE FROM {tablename} WHERE billno = '{billno}'  AND company = '{company}'")


def verify_exists_data(company, dbname, tablename, kdata):
    with SqliteDBManager(dbname) as sqlitemanager:
        result = sqlitemanager.execute(
            f"SELECT 1 FROM {tablename} WHERE company = '{company}' AND billno = '{kdata[1]}'", fetch=True)

    return result


def ProductionGZ(company, dbname, tablename):
    jdy_api = JDYApi(Common.api_key, Common.app_id)
    log = Logger('main', 'production.log')

    # 获取金蝶销售出库数据
    with MSSqlDBManager(company) as msmanager:
        kdata = msmanager.execute(Common.ProductionGZ_query_sql, fetch=True)

    # 将最新数据插入本地Sqlite临时表temp中
    with SqliteDBManager(dbname) as sqlitemanager:
        # 插入前先清除缓存表数据
        sqlitemanager.execute('DELETE FROM temp')
        sqlitemanager.execute(Common.insert_temp_sql, params=kdata)

    # 在sqlite中比对两侧数据
    # 比对删除数据，删除被同步端数据
    with SqliteDBManager(dbname) as sqlitemanager:
        query_sql = Common.deleted_query_sql.format(company=company)
        deleted_kdata = sqlitemanager.execute(query_sql, fetch=True)
    if deleted_kdata:
        # 删除简道云数据
        delete_jdy_data( jdy_api, deleted_kdata)
        # 同时删除sqlite映射数据
        delete_sqlite_data( dbname, tablename, deleted_kdata)
        log.info('deleted_kdata: ' + str(deleted_kdata))
    # 比对更新和增量数据，同步数据（同步时校验被同步端是否存在，存在则删除后同步最新数据）
    with SqliteDBManager(dbname) as sqlitemanager:
        diff_sql = Common.differences_sql.format(company=company)
        diff_data = sqlitemanager.execute(diff_sql, fetch=True)
        differences = [list(tup) for tup in diff_data]

    # 处理更新数据
    if differences:
        for diff in differences:
            res = verify_exists_data(company, dbname, tablename, diff)
            # 简道云存在数据，调用jdy更新接口
            if res:
                update_data = utils.update_data_process(diff, Common.jdy_update_data)
                result = jdy_api.update_data(update_data)
                # 同时处理本地映射sqlite
                if result:
                    print(result)
                    # 插入前先删除历史数据
                    delete_sqlite_data( dbname, tablename, diff)
                    # 将最新数据插入本地Sqlite映射表中
                    with SqliteDBManager(dbname) as sqlitemanager:
                        sqlitemanager.execute(Common.insert_production_sql, params=[diff])
            else:
                # 简道云不存在，调用jdy批量新增接口
                upload_data = utils.upload_data_process(diff, Common.jdy_production_data)
                result = jdy_api.upload(upload_data)
                if result:
                    log.info("简道云上传结果：" + str(diff))
                    # 将最新数据插入本地Sqlite映射表中
                    with SqliteDBManager(dbname) as sqlitemanager:
                        print("diff: " + str(diff))
                        sqlitemanager.execute(Common.insert_production_sql, params=[diff])
    else:
        log.info('本次查询无上传数据，简道云同步任务结束！！！')



# if __name__ == '__main__':
#     company = '希肤广州'
#     dbname = 'production.db'
#     tablename = 'production'
#     ProductionGZ(company, dbname, tablename)

