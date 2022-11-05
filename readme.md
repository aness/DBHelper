## WHAT IS THIS DBHelper Class

Its just a wrapper class for the python mysql connector library 
 The original Mysql connector doc is at https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

 #What this do is simplify everything and just Read or Write and makes things more clean espessialy the connect-disconnect  at the end 

 #Note: his does not keep a open tcp Session connection with the server (it's more like a hit and run strategy that ensures less stress on the DB server if used from multiple locations, not optimal for you if you are working on server-side)

    1) Connects To DB Server
    2) Execute (SQL) 
    3) Save results 
    4) Disconnects from the Server [THIS IS MORE FOR CRONS]
    5) Returns results 




## HOW TO USE 
- Include The Core/dbhelper.py file in your project.
- Just import and create a DBHelper object with :
    mydb = mydbHelper('YOUR_HOST_HERE', 'USERNAME_HERE', 'PWD_HERE', 'DATABASE_HERE')

#### READ FROM DB (SELECT):
resulting_rows = mydb.read('SELECT * FROM YOURTABLE')

#### WRITE TO DB (INSERT):
mydb.exec("INSERT INTO YOURTABLE(FIELD) VALUES('VAL');")






