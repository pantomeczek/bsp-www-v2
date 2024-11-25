import psycopg2

class PostgresConn:

    connection = None
    cursor = None

    def __init__(self):
        self.connection = psycopg2.connect(database="bspotlight", 
                                           user='bspotlight', 
                                           password='motorolla', 
                                           host='34.41.120.246', 
                                           port= '5432'
                                          )
        self.cursor = self.connection.cursor()
    

    def get_cursor_to_pg(self):
        return self.cursor

    def close_cursor(self):
        self.cursor.close()

    def close_connection(self):
        self.connection.close()
