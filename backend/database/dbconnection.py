import psycopg2

def dbconn():

    try:
        conn = psycopg2.connect(
        host="192.168.88.129",
        database="ct526",
        user="test",
        password="password",
        port="5432"
        )
        print("Database's Connected ")
    
    except:
        print("Error connecting to the database")
 
    
    return conn  



'''class dbconnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="192.168.159.134",
            database="ct526",
            user="test",
            password="password",
            port="5432"
        )
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                password VARCHAR(255)
            )
                         
        """)
        self.conn.commit()

    def insert_user(self, name, email, password):
        self.cur.execute("""
            INSERT INTO users (name, email, password) VALUES (%s, %s, %s)
        """, (name, email, password))
        self.conn.commit()

    def get_users(self):
        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()

    def close_connection(self):
        self.cur.close()
        self.conn.close()  


        '''