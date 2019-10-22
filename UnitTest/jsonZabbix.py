import json

from pyzabbix import ZabbixAPI

import config

# stream = logging.StreamHandler(sys.stdout)
# stream.setLevel(logging.DEBUG)
# log = logging.getLogger('pyzabbix')
# log.addHandler(stream)
# log.setLevel(logging.DEBUG)
zapi = ZabbixAPI(config.zbx_server)


def zabbix_request(search_name, hostid):
    zapi.session.verify = config.zbx_api_verify
    zapi.login(config.zbx_user, config.zbx_password)
    json_items = zapi.do_request('item.get',
                                 {
                                     'output': ['itemid', 'name'],
                                     'hostids': hostid,
                                     'search': {
                                         'name': search_name
                                     }
                                 }
                                 )
    if json_items['result']:
        itemid = json_items['result'][0]['itemid']
        item_name = json_items['result'][0]['name']
        json_trend = zapi.do_request('trend.get',
                                     {
                                         'output': ['itemid', 'clock', 'value_avg'],
                                         'itemids': itemid,
                                         'time_from': config.time_from,
                                         'time_till': config.time_to
                                     }
                                     )
        print("Host: " + hostid)
        print("Item: " + item_name)
        print(json.dumps(json_trend, indent=4, sort_keys=True))
        print(json_trend)
        # return json_trend


if __name__ == '__main__':
    zabbix_request('Available memory in percentage', '10272')
    zapi.user.logout()
