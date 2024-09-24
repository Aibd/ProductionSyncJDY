from ProductionGZ import ProductionGZ
from apscheduler.schedulers.blocking import BlockingScheduler
import random


def salesorder_function():
    companygz = '希肤广州'
    companysh = '希肤上海'
    dbname = 'production.db'
    tablename = 'production'
    ProductionGZ(companygz, dbname, tablename)


if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(salesorder_function, 'interval', minutes=random.randint(10, 30))
    sched.start()
