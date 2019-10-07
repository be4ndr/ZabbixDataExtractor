import time

mssql_server = 'MSSQLServer'
db_name = 'DB1'
trusted_connection = 'Trusted_Connection=yes;'
mssql_user = 'sqluser'
mssql_pass = 'sqlpass'

zbx_server = 'MyZbxServer'
zbx_user = 'zbxuser'
zbx_password = 'zbxpass'
zbx_prefix = 'zde'
zbx_tmp_dir = '/tmp' + zbx_prefix
zbx_api_verify = False
items = {'item1', 'item2'}
time_from = time.time() - 86400
time_to = time.time()
