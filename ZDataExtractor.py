import pyodbc
from pyzabbix import ZabbixAPI

import config

zapi = ZabbixAPI(config.zbx_server)
sql_server = "{SQL Server}"


def mssql_insert_json(json_dir, table_name):
    conn = pyodbc.connect(f'Driver={sql_server};SERVER={config.mssql_server};DATABASE={config.db_name};UID={config.mssql_user};PWD={config.mssql_pass}')
    cursor = conn.cursor()
    json_length = len(json_dir['result'])
    for i in range(0, json_length):
        item_fields = {key: ''.join(values) for key, values in json_dir['result'][i].items()}
        sql = f"INSERT INTO {table_name} (UTCTime, Itemid, Value) VALUES (?, ?, ?)"
        params = (
            item_fields['clock'],
            item_fields['itemid'],
            item_fields['value_avg'],
        )
        cursor.execute(sql, params)
        conn.commit()


def zabbix_request(search_name, hostid):
    json_items = zapi.do_request('item.get',
                                 {
                                     'output': ['itemid', 'name'],
                                     'hostids': hostid,
                                     'search': {
                                         'name': search_name
                                     }
                                 }
                                 )
    if search_name.__eq__('CPU usage. Average 5 min.'):
        table_name = 'CPUData'
    else:
        table_name = 'MemoryData'
    if json_items['result']:
        itemid = json_items['result'][0]['itemid']
        json_trend = zapi.do_request('trend.get',
                                     {
                                         'output': ['itemid', 'clock', 'value_avg'],
                                         'itemids': itemid,
                                         'time_from': config.time_from,
                                         'time_till': config.time_to
                                     }
                                     )
        mssql_insert_json(json_trend, table_name)


if __name__ == '__main__':
    zapi.session.verify = config.zbx_api_verify
    zapi.login(config.zbx_user, config.zbx_password)
    for h in zapi.host.get(output="extend"):
        for i in config.items:
            zabbix_request(i, h['hostid'])
    zapi.user.logout()
    print("----------------------")
    print("Job done successfully!")
