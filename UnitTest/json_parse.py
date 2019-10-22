import UnitTest.jsonZabbix

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
