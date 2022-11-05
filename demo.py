from Core.dbHelper import DBHelper

writing_req = "INSERT INTO something(field1,field2,field3) VALUES('v1','v2','v3');"
reading_req = 'SELECT * FROM something'

mydb = DBHelper('YOUR_HOST_HERE', 'USERNAME_HERE',
                  'PWD_HERE', 'DATABASE_HERE')

results_rows = mydb.read(reading_req)
for row in results_rows:
    print(' A row :'+str(row))

mydb.exec(writing_req)

