from datetime import datetime
import pymssql
from elasticsearch import Elasticsearch
from elasticsearch import helpers

BULK_SIZE = 50000

es = Elasticsearch('172.16.13.26:9206', timeout=120)

conn = pymssql.connect(server='172.16.8.10\RICESTSQLSERVER', user='sa', password='RICEST@SQLSERVER2008', database='NOSQL_db')  
cursor = conn.cursor()

cursor.execute('SELECT ID, DocID, Abstract FROM [NOSQL_db].[dbo].[LangFilter]')
sum = 0
bulks = 0
actions = []
for item in cursor:
    actions += [
        {
            "_index": "nosqlprj-3shard",
            "_type": "records",
            "_id": item[0],
            "_source": {
                "DocID": item[1],
                "Abstract": item[2]
            }
        },
        {
            "_index": "nosqlprj-6shard",
            "_type": "records",
            "_id": item[0],
            "_source": {
                "DocID": item[1],
                "Abstract": item[2]
            }
        }
    ]
    sum+=1
    if sum == BULK_SIZE:
        bulks += 1
        sum = 0
        helpers.bulk(es, actions)
        actions = []
        print ("\rNo of bulks inserted: %d" % bulks, end="")

cursor.execute('SELECT TOP (3000000) ID, DocID, Abstract FROM [NOSQL_db].[dbo].[LangFilterIEEE]') # 3 Mil
sum = 0
bulks = 0
actions = []
for item in cursor:
    actions += [
        {
            "_index": "nosqlprj-3shard",
            "_type": "records",
            "_id": item[0],
            "_source": {
                "DocID": item[1],
                "Abstract": item[2]
            }
        },
        {
            "_index": "nosqlprj-6shard",
            "_type": "records",
            "_id": item[0],
            "_source": {
                "DocID": item[1],
                "Abstract": item[2]
            }
        }
    ]
    sum+=1
    if sum == BULK_SIZE:
        bulks += 1
        sum = 0
        helpers.bulk(es, actions)
        actions = []
        print ("\rNo of IEEE bulks inserted: %d" % bulks, end="")