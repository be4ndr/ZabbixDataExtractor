import logging
import sys

import pyodbc

import config

stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logging.DEBUG)
sql_server = "{SQL Server}"
json_dir_data = {
    "clock": "1568919600",
    "itemid": "29904",
    "value_avg": "26.5876"
}
json_dir_data1 = {'jsonrpc': '2.0',
                  'result': [{'itemid': '29904', 'clock': '1569268800', 'value_avg': '27.5254'}, {'itemid': '29904', 'clock': '1569272400', 'value_avg': '27.6691'},
                             {'itemid': '29904', 'clock': '1569276000', 'value_avg': '27.9442'}, {'itemid': '29904', 'clock': '1569279600', 'value_avg': '28.1550'},
                             {'itemid': '29904', 'clock': '1569283200', 'value_avg': '28.1480'}, {'itemid': '29904', 'clock': '1569286800', 'value_avg': '27.6145'},
                             {'itemid': '29904', 'clock': '1569290400', 'value_avg': '27.7776'}, {'itemid': '29904', 'clock': '1569294000', 'value_avg': '27.8386'},
                             {'itemid': '29904', 'clock': '1569297600', 'value_avg': '27.7885'}, {'itemid': '29904', 'clock': '1569301200', 'value_avg': '27.6612'},
                             {'itemid': '29904', 'clock': '1569304800', 'value_avg': '27.3322'}, {'itemid': '29904', 'clock': '1569308400', 'value_avg': '27.2629'},
                             {'itemid': '29904', 'clock': '1569312000', 'value_avg': '27.1978'}, {'itemid': '29904', 'clock': '1569315600', 'value_avg': '27.2832'},
                             {'itemid': '29904', 'clock': '1569319200', 'value_avg': '26.8689'}, {'itemid': '29904', 'clock': '1569322800', 'value_avg': '26.6862'},
                             {'itemid': '29904', 'clock': '1569326400', 'value_avg': '26.7178'}, {'itemid': '29904', 'clock': '1569330000', 'value_avg': '26.6058'},
                             {'itemid': '29904', 'clock': '1569333600', 'value_avg': '26.7103'}, {'itemid': '29904', 'clock': '1569337200', 'value_avg': '26.9855'},
                             {'itemid': '29904', 'clock': '1569340800', 'value_avg': '27.0110'}, {'itemid': '29904', 'clock': '1569344400', 'value_avg': '27.1071'},
                             {'itemid': '29904', 'clock': '1569348000', 'value_avg': '26.8511'}], 'id': 2}


def mssql_insert_json(json_dir, table_name):
    json_length = len(json_dir['result'])
    params = ''
    for i in range(0, json_length):
        item_fields = {key: ''.join(values) for key, values in json_dir['result'][i].items()}
        params = (
            item_fields['clock'],
            item_fields['itemid'],
            item_fields['value_avg'],
        )
    sql = f"INSERT INTO {table_name} (UTCTime, Itemid, Value) VALUES (?, ?, ?)"
    cursor.execute(sql, params)


if __name__ == '__main__':
    conn = pyodbc.connect(f'Driver={sql_server};SERVER={config.mssql_server};DATABASE={config.db_name}')
    cursor = conn.cursor()
    mssql_insert_json(json_dir_data1, 'CPUData')
    conn.commit()
