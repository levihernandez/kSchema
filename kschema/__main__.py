AUTHOR = '''
Julian Levi - 5/8/20
'''

DOCS = '''
namespace: a fully qualified name that avoids schema naming conflicts
type: Avro data type, for example, record, enum, union, array, map, or fixed
name: unique schema name in this namespace
fields: one or more simple or complex data types for a record. The first field in this record is called id, and it is of type string. The second field in this record is called amount, and it is of type double.
'''

SCHEMA = '''
Generate AVRO Schema
{"namespace": "io.confluent.examples.clients.basicavro",
 "type": "record",
 "name": "Payment",
 "fields": [
     {"name": "id", "type": "string"},
     {"name": "amount", "type": "double"}
 ]
}
'''

import sqlite3
import json
import sqlite as s

conn = sqlite3.connect('data/db/kschema_demo.db')
c = conn.cursor()


data = {}
data['type'] = "record"
data['namespace'] = "com.aumersdata.avro.record"
data['name'] = "Fields"
data['fields'] = {}
t = ('demo1')
tr = c.execute('PRAGMA table_info(' + t + ')')
fields = []
for r in tr:
    # Test data type & replace proper avro data type
    namae = r[1]
    typeo = r[2]
    too = s.Sqlite(typeo)
    to = too.returntype()
    # print(namae, str(to))
    fr = {'name': namae, 'type': to}
    fields.append(fr)

data['fields'] = fields
json_data = json.dumps(data, indent=2)
print(json_data)

