import xlrd, pymssql, os

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

# Give the location of the file 
loc = ("lastSundayResult/fulltextresults.xlsx") 
destination_dir = "excel_item_abstracts"
os.system("mkdir -p %s" % destination_dir)

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
already_exists = 0
created = 0
for i in range(1, 81):
    for j in range(4, 9):
        cell = sheet.cell_value(i, j)
        if (str(cell) == ""):
            break
        id = int(float(str(cell)))
        try:
            with open("%s/%d.txt" % (destination_dir,id), "x") as f:
                print("%s" % getdoc(id), file=f)
                created += 1
        except FileExistsError:
            already_exists += 1

print("%d items already exists, %d items created." % (already_exists, created))