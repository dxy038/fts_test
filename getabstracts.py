import pymssql, os

conn = pymssql.connect(server='172.16.8.10\RICESTSQLSERVER', user='sa', password='RICEST@SQLSERVER2008', database='NOSQL_db')  
cursor = conn.cursor()

def getdoc(ID):
    global cursor
    cursor.execute('SELECT Abstract FROM [NOSQL_db].[dbo].[LangFilterIEEE] WHERE ID = %d' % ID)
    for item in cursor:
        return str(item[0])
    cursor.execute('SELECT Abstract FROM [NOSQL_db].[dbo].[LangFilter] WHERE ID = %d' % ID)
    for item in cursor:
        return str(item[0])

def extractAbstracts(ref):
    times = []
    created = 0
    already_exists = 0
    with open(ref,"r") as file1:
        line_no = 0
        while True:
            line = file1.readline()
            line_no += 1
            print("\r REF = %s | PROCESSING LINE %d             " % (ref, line_no), end="")
            if line == "":
                break
            id = int(line.rstrip())
            try:
                with open("./lastFetchedResults-Abstracts/%d.txt" % (id), "x") as f:
                    print("%s" % getdoc(id), file=f)
                    created += 1
            except FileExistsError:
                already_exists += 1
    return (created, already_exists)

refs = ["and-elastic5results.txt","and-mongoresults.txt","and-mssqlresults.txt", "and-mysqlresults.txt",
            "single-elastic5results.txt","single-mongoresults.txt","single-mssqlresults.txt", "single-mysqlresults.txt",
            "or-elastic5results.txt","or-mongoresults.txt","or-mssqlresults.txt", "or-mysqlresults.txt",
            "exactphrase-elastic5results.txt","exactphrase-mongoresults.txt","exactphrase-mssqlresults.txt", "exactphrase-mysqlresults.txt"]

created = 0
already_exists = 0
for r in refs:
    re = extractAbstracts("./lastFetchedResults-IDs/"+r)
    created += re[0]
    already_exists += re[1]

print ("\n%d Created %d Already Exists" % (created, already_exists))