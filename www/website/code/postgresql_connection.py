import psycopg2
import os
import socket

db_config = {
    "PROD": {
        "database": "bspotlight",
        "user": "bspotlight",
        "password": "motorolla",
        "host": "localhost",
        "port": "5432"
    },
    "DEV": {
        "database": "bspotlight",
        "user": "bspotlight",
        "password": "motorolla",
        "host": "192.168.10.170",
        "port": "32001"
    }
}

class PostgresConn:

    connection = None
    cursor = None

    def __init__(self):
        hostname = socket.gethostname()
        env = "PROD" if hostname == "blockspotlight" else "DEV"
        conn_details = db_config.get(env)
        self.connection = psycopg2.connect(database=conn_details.get("database"), 
                                           user=conn_details.get("user"), 
                                           password=conn_details.get("password"), 
                                           host=conn_details.get("host"), 
                                           port= conn_details.get("port"), 
                                          )
        self.cursor = self.connection.cursor()
    

    def get_cursor_to_pg(self):
        return self.cursor

    def close_cursor(self):
        self.cursor.close()

    def close_connection(self):
        self.connection.close()
