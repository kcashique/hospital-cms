import psycopg2


db_conn = psycopg2.connect(
            dbname="hospitel_test_db",
            user="postgres",
            password="postgress",
            host="localhost",
            port="5432"
        )

