#WHAT IS THIS DBHelper 

Its just a wrapper class for the python mysql connector library 
 The connector doc is at https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

 #What this do is simplify everything and just Read or Write and makes things more clean espessialy the connect-disconnect  at the end 

 #Look this doesnt keep a tcp open connection with the server it closes the connection 

 1) Connects To DB Server
 2) Execute (SQL) 
 3) Save results 
 4) Disconnects from the Server
 5) Returns results 


#HOW TO USE 
Just import and create a DBHelper object with :
    mydb = mydbHelper('YOUR_HOST_HERE', 'USERNAME_HERE', 'PWD_HERE', 'DATABASE_HERE')

#TO READ FROM SELECT 
resulting_rows = mydb.read('SELECT * FROM YOURTABLE')

#TO EXECUTE INSERT
mydb.exec("INSERT INTO YOURTABLE(FIELD) VALUES('VAL');")

I plan to use this in my projets to make it simple 


