import UnitTest.jsonZabbix

# json_dir_data = {'jsonrpc': '2.0', 'result': [{'itemid': '29904', 'clock': '1569268800', 'value_avg': '27.5254'}, {'itemid': '29904', 'clock': '1569272400', 'value_avg': '27.6691'}], 'id': 2}

if __name__ == '__main__':
    json_dir = UnitTest.jsonZabbix.zabbix_request('Available memory in percentage', '10272')
    item_fields = {
        'clock': [],
        'itemid': [],
        'value_avg': []
    }
    json_length = len(json_dir['result'])
    for i in range(0, json_length):
        item_fields = {key: ''.join(values) for key, values in json_dir['result'][i].items()}
        print(item_fields)
