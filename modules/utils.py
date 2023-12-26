import psycopg2
from modules.db_config import db_conn



def get_user(self):
    try:
        cur =db_conn.cursor()
        cur.execute("SELECT user_id, user_name, db_token FROM user_tbl WHERE db_token = (%s)", (self.browser_token))
        result = cur.fetchall()
        cur.close()
    except psycopg2.Error as e:
        print (f'DB_ERROR:{e.pgerror}')
    
    if len(result)==0:
        print ("user token is invalid")
    else:
        user_data = [{"user_id":row[0], "user_name":row[1], "db_token":row[2]} for row in result]
    if self.browser_token == user_data[0]['db_token']:
        print (f"hello mr.{user_data[0]['user_name']}.")
        
    return user_data[0]['db_token']
