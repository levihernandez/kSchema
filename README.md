# kSchema - Kafka Registry Generator

## Database

A small sample demonstrates how to extract DB tables onto AVRO Schemas.

Using SQLite, connect to the database and extract the DDL information in order to build the AVRO schema.

> Download project 

`git clone https://github.com/levihernandez/kSchema.git`

> Create SQLite DB to test script

```bash
$ sqlite3 data/db/kschema_demo.db
SQLite version 3.28.0 2019-03-02 15:25:24
Enter ".help" for usage hints.
sqlite> CREATE TABLE demo1 (
    id INTEGER NOT NULL,
    name INTEGER,
    "last" INTEGER,
    price NUMERIC)'
sqlite> insert into demo1 values(1, 'John','doe', 12322.12);
sqlite> insert into demo1 values(2, 'Jane','doe', 12322);
(1, 'John', 'Doe', 234.99)
(2, 'Jane', 'Doe', 10000.03)
```

> Run Python script as a package

`$ python3 kschema`

```json
{
  "type": "record",
  "namespace": "com.aumersdata.avro.record",
  "name": "Fields",
  "fields": [
    {
      "name:": "id",
      "type": "int"
    },
    {
      "name:": "name",
      "type": "int"
    },
    {
      "name:": "last",
      "type": "int"
    },
    {
      "name:": "price",
      "type": "float"
    }
  ]
}
```
