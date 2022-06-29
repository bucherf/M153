import psycopg2, sys
 
modulename = 'psycopg2'
if 'psycopg2' not in modulename:
    print('Module not loaded')
 
def connect():
    try:
        conn = psycopg2.connect(host="localhost",
        database="customers",
        user="postgres",
        password="postgres",
        port="8080")
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n')
        print(e)
        sys.exit(1)
    else:
        print('Connected!')

connect()