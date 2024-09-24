import uuid
from copy import deepcopy
from jdy import JDYApi


# 金蝶字段转换为简道云对应值的字段编号
def kdata_field_to_jdy(kingdee_data):
    # 简道云表单查询接口调用
    api_key = "1ENC5lt8m3pf97kiKnATic26eTIXQKR5"
    app_id = "65bc6159daf9cea1dbb5be86"
    jdy_api = JDYApi(api_key, app_id)
    users = jdy_api.get_usernumber()
    # 制单替换为简道云用户
    if kingdee_data[27] in users.keys():
        kingdee_data[27] = users[kingdee_data[27]]
    else:
        kingdee_data[27] = users['张木森']  # 处理键不存在的情况
    # 销售代表人员替换为简道云用户
    if kingdee_data[28] in users.keys():
        kingdee_data[28] = users[kingdee_data[28]]
    else:
        kingdee_data[28] = users['张木森']
    # 销售助理人员替换为简道云用户
    if kingdee_data[29] in users.keys():
        kingdee_data[29] = users[kingdee_data[29]]
    else:
        kingdee_data[29] = users['张木森']
    # 生产主管人员替换为简道云用户
    if kingdee_data[30] in users.keys():
        kingdee_data[30] = users[kingdee_data[30]]
    else:
        kingdee_data[30] = users['张木森']
    # 品质主管人员替换为简道云用户
    if kingdee_data[31] in users.keys():
        kingdee_data[31] = users[kingdee_data[31]]
    else:
        kingdee_data[31] = users['张木森']
    return kingdee_data


# 金蝶数据转换为简道云接口payload数据包格式
def upload_data_process(kingdee_raw_data, jdy_data):
    kingdee_data = deepcopy(kingdee_raw_data)
    kdata = kdata_field_to_jdy(kingdee_data)
    print(kdata)
    jdy_data["transaction_id"] = str(uuid.uuid4())
    data_dict = jdy_data['data_list'][0]
    fields = list(data_dict.keys())
    upload_data = deepcopy(data_dict)
    for field, new_value in zip(fields, kdata):
        upload_data[field]["value"] = new_value

    jdy_data['data_list'] = [upload_data]
    return jdy_data


# 金蝶数据转换为简道云接口payload数据包格式
def update_data_process(kingdee_raw_data, jdy_data):
    kingdee_data = deepcopy(kingdee_raw_data)
    kdata = kdata_field_to_jdy(kingdee_data)
    jdy_data["transaction_id"] = str(uuid.uuid4())
    data_dict = jdy_data['data']
    fields = list(data_dict.keys())
    update_data = deepcopy(data_dict)
    for field, new_value in zip(fields, kdata):
        update_data[field]["value"] = new_value

    jdy_data['data'] = update_data
    return jdy_data
