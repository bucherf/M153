#suche für content
#eingabevalidierung und user feedback zb 'feld darf nicht leer sein'
#register user and admin can delete
from email.policy import strict
from operator import truediv
import string
from db import Db
import psycopg2
from config import dbConfig

class eventDAO():

    def __init__(self):
        self.db = Db()

    def __send_sql(self, sql):
        conn = None        
        try:
            params = dbConfig()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql)
            if "SELECT" in sql:
                res = cur.fetchall()
                print(res)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def create_user(self, vorname, nachname, land_id):
        sql ="INSERT INTO users(vorname, nachname, land_id) VALUES ('" + vorname + "','" + nachname + "'," + land_id + ")"
        self.__send_sql(sql)

    def read_user(self,id):
        sql ="SELECT vorname, nachname, land_id FROM users WHERE users.id = " + id
        self.__send_sql(sql)
    
    def update_user(self, vorname, nachname, land_id, user_id):
        sql ="UPDATE users SET vorname = '" + vorname + "', nachname = '" + nachname + "', land_id = " + land_id + " WHERE id = " + user_id + ";"
        print(sql)
        self.__send_sql(sql)
    
    def delete_user(self,id):
        sql ="DELETE FROM users WHERE users.id =" + id
        self.__send_sql(sql)
    
    def create_event(self, beschreibung, name, kategorie_id):
        sql ="INSERT INTO event(beschreibung, name, kategorie_id) VALUES ('" + beschreibung + "', '" + name + "', " + kategorie_id + ")"
        self.__send_sql(sql)

    def read_event(self,id):
        sql ="SELECT beschreibung, name, kategorie_id FROM event WHERE event.id = " + id
        self.__send_sql(sql)
    
    def update_event(self, beschreibung, name, kategorie_id, event_id):
        sql ="UPDATE event SET beschreibung = '" + beschreibung + "', name = '" + name + "', kategorie_id = " + kategorie_id + " WHERE id = " + event_id + ";"
        self.__send_sql(sql)
    
    def delete_event(self,id):
        sql ="DELETE FROM event WHERE event.id = " + id
        self.__send_sql(sql)
    
    def search(self, spalte, tabelle):
        sql ="SELECT '" + spalte + "' FROM '" + tabelle + "' WHERE     "

eventdao = eventDAO()

print('What do you want to do:')
print('cu    create user')
print('ru    read user')
print('uu    update user')
print('du    delete user')
print('ce    create event')
print('re    read event')
print('ue    update event')
print('de    delete event')
print('s     search')



toDo = input()
if toDo == 'cu':
    print("Please enter the first name: ")
    i_vorname = input()
    print("Please enter the last name: ")
    i_nachname = input()
    print("Please enter the land_id: ")
    i_land_id = input()
    if i_land_id.isnumeric():
        eventDAO.create_user(eventdao, i_vorname, i_nachname, i_land_id)
    else:
        print("land_id must be a number!")

elif toDo == 'ru':
    print("Please enter the id of the user you want to read: ")
    i_id_ru = input()
    eventDAO.read_user(eventdao, i_id_ru)

elif toDo == 'uu':
    print("Please enter the id of the user that you want to update")
    i_id_uu = input()
    print("Please update the first name: ")
    i_vorname_u = input()
    print("Please update the last name: ")
    i_nachname_u = input()
    print("Please update the land_id: ")
    i_land_id_u = input()
    eventDAO.update_user(eventdao, i_vorname_u, i_nachname_u, i_land_id_u, i_id_uu)

elif toDo == 'du':
    print("Please enter the id of the user you want deleted: ")
    i_id_du = input()
    eventDAO.delete_user(eventdao, i_id_du)

elif toDo == 'ce':
    print("Please enter the description of the event: ")
    i_beschreibung = input()
    print("Please enter the name of the event: ")
    i_name = input()
    print("Please enter the kategorie_id of the event: ")
    i_kategorie_id = input()
    eventDAO.create_event(eventdao, i_beschreibung, i_name, i_kategorie_id)

elif toDo == 're':
    print("Please enter the id of the event you want to read: ")
    i_id_re = input()
    eventDAO.read_event(eventdao, i_id_re)

elif toDo == 'ue':
    print("Please enter the id of the event that you want to update")
    i_id_ue = input()
    print("Please update the description: ")
    i_beschreibung_u = input()
    print("Please update the name: ")
    i_name_u = input()
    print("Please update the kategorie_id: ")
    i_kategorie_id_u = input()
    eventDAO.update_event(eventdao, i_beschreibung_u, i_name_u, i_kategorie_id_u, i_id_ue)

elif toDo == 'de':
    print("Please enter the id of the event you want deleted: ")
    i_id_de = input()
    eventDAO.delete_event(eventdao, i_id_de)

elif toDo == 's':
    eventDAO.search()        
else:
    print('wrong command')