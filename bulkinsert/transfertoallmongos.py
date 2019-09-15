import pymongo
import pymssql

SQL_EXPORT_DB = 'nosqlprj'
RECORDS_COL = 'records'

# client = pymongo.MongoClient('mongodb://172.16.13.26:27023/')
# mydb = client[SQL_EXPORT_DB]
# mycol = mydb[RECORDS_COL]

client_3sh = pymongo.MongoClient('mongodb://172.16.13.26:27030/', retryWrites=False)
mydb_3sh = client_3sh[SQL_EXPORT_DB]
mycol_3sh = mydb_3sh[RECORDS_COL]

# client_6sh = pymongo.MongoClient('mongodb://172.16.13.26:27032/', retryWrites=False)
# mydb_6sh = client_6sh[SQL_EXPORT_DB]
# mycol_6sh = mydb_6sh[RECORDS_COL]

conn = pymssql.connect(server='172.16.8.10\RICESTSQLSERVER', user='sa', password='RICEST@SQLSERVER2008', database='NOSQL_db')  
cursor = conn.cursor()
 
cursor.execute('SELECT ID, DocID, Abstract FROM [NOSQL_db].[dbo].[LangFilter]')

sum = 0

for item in cursor:
    new_dict = {}
    new_dict['_id'] = item[0]
    new_dict['DocID'] = item[1]
    new_dict['Abstract'] = item[2]
    # mycol.insert_one(new_dict)
    mycol_3sh.insert_one(new_dict)
    # mycol_6sh.insert_one(new_dict)
    sum+=1
    print("\r %d items migrated to Mongo." % sum, end="")

cursor.execute('SELECT TOP(3000000) ID, DocID, Abstract FROM [NOSQL_db].[dbo].[LangFilterIEEE]')

for item in cursor:
    new_dict = {}
    new_dict['_id'] = item[0]
    new_dict['DocID'] = item[1]
    new_dict['Abstract'] = item[2]
    # mycol.insert_one(new_dict)
    mycol_3sh.insert_one(new_dict)
    # mycol_6sh.insert_one(new_dict)
    sum+=1
    print("\r %d items migrated to Mongo." % sum, end="")