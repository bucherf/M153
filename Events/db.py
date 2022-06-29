#from turtle import circle
#from typing_extensions import Self
import psycopg2
from config import dbConfig

class Db:
    connection = None

    def getConnection(self):
        if self.connection == None:
            self.connect()
        return self.connection

    def connect(self):
        self.connection = None
        
        try:

            params = dbConfig()

            print('Connecting to the PostgreSQL database...')
            self.connection = psycopg2.connect(**params)

            self.connection.set_client_encoding('1252')
            cur = self.connection.cursor()
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            dbVersion = cur.fetchone()
            print(dbVersion)

        except (Exception,psycopg2.DatabaseError) as error :
            print(error)

        finally: 
        
            cur.close()

    def query(self,string):
        self.getConnection()
        try:
            cur = self.connection.cursor()
            cur.execute(string)
            self.connection.commit()
        except (Exception,psycopg2.DatabaseError) as error :
            print(error)
        finally:
            cur.close()

    def queryValues(self,string,values):
        self.getConnection()

        try:
            cur = self.connection.cursor()
            cur.execute(string,values)
            self.connection.commit()
        except (Exception,psycopg2.DatabaseError) as error :
            print(error)
        finally:
            cur.close()

    def closeConnection(self):
        self.connection.close()
        self.connection = None


if __name__ == '__main__':
    Db.connect()