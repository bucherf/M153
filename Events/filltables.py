import psycopg2
from config import dbConfig

class fillTables:


    def insert(self):


        sql = '''
        INSERT INTO land(bezeichnung) VALUES ('Schweiz');
        INSERT INTO land(bezeichnung) VALUES ('Deutschland');
        INSERT INTO kategorie(bezeichnung) VALUES ('HipHop');
        INSERT INTO kategorie(bezeichnung) VALUES ('Techno');
        INSERT INTO users(vorname, nachname, land_id) VALUES ('Max', 'Muster', '1');
        INSERT INTO users(vorname, nachname, land_id) VALUES ('Maxime', 'Mustermann', '2');
        INSERT INTO event(beschreibung, name, kategorie_id) VALUES ('Das ist ein HipHop Festival','OAFF', '1');
        INSERT INTO event(beschreibung, name, kategorie_id) VALUES ('Das ist ein Techno Festival','OAFF', '2');
        INSERT INTO teilnehmer(users_id, event_id) VALUES ('1','1');
        INSERT INTO teilnehmer(users_id, event_id) VALUES ('2','2');'''
        conn = None

        
        try:
            params = dbConfig()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == "__main__":
    filltables = fillTables()
    filltables.insert()