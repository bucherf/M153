from db import Db
import psycopg2
from config import dbConfig

def create_tables():
    sql ="""CREATE TABLE land (
        id                  SERIAL PRIMARY KEY,
        bezeichnung         VARCHAR(255)
        );

        CREATE TABLE kategorie (
        id                  SERIAL PRIMARY KEY,
        bezeichnung         VARCHAR(255)
        );
    
        CREATE TABLE users (
        id                  SERIAL PRIMARY KEY,
        vorname             VARCHAR(255),
        nachname            VARCHAR(255),
        land_id             int references land(id)
        );

        CREATE TABLE event (
        id                  SERIAL PRIMARY KEY,
        beschreibung        VARCHAR(255),
        name                VARCHAR(255),
        kategorie_id        int references kategorie(id)
        );

        CREATE TABLE teilnehmer (
        users_id            int references users(id),
        event_id            int references event(id)
        );"""

    conn = None
    try:
        params = dbConfig()
        conn = psycopg2.connect(**params)
        #conn.set_client_encoding('1252')
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()