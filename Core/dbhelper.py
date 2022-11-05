import sys
import os
import time
import threading
import mysql.connector


class DBHelper():
    host = "localhost"
    user = "login"
    password = "password"
    database = "demo_python"
    currentsql = "select id, nom, score, date_inscription, actif from utilisateur"
    state = ""

    def __init__(self, host, user, password, database):
        self.state = "_initializing"
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def init(self):
        self.state = "initializing"

    def start(self):
        self.state = "starting"

    def read(self, sqlcode):
        self.state = "reading"
        print('trying to connect to '+self.host)
        cnx = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        cursor = cnx.cursor()
        cursor.execute(sqlcode)
        rslt = cursor.fetchall()


        cnx.close()
        return rslt
    
    def exec(self, sqlcode):
        self.state = "reading"
        print('trying to connect to '+self.host)
        cnx = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        cursor = cnx.cursor()
        cursor.execute(sqlcode)
        cnx.commit()


        cnx.close()
        return rslt 
