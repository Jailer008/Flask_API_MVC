from app.db import get_db_connection
from app.config import Config

table = Config.DB_NAME + ".users"

def get_user(user_id):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM " + table + " WHERE id = " + user_id
            cursor.execute(sql)
            result = cursor.fetchone()
    return result
def save_user(user_id, user_name):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO " + table + " (id,name) VALUES (%s, %s)"
            try:
                cursor.execute(sql, (user_id, user_name))
            except:
                return {}
        connection.commit()
    return {'user_id': user_id, 'user_name': user_name, 'status': 'saved'}

def update_user(user_id, user_name):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE " + table + " SET name = %s WHERE id = %s"
            cursor.execute(sql, (user_name, user_id))
            connection.commit()
            if cursor.rowcount == 0:
                return None
    return {'user_id': user_id, 'user_name': user_name, 'status': 'updated'}

def delete_user(user_id):
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM " + table + " WHERE id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            if cursor.rowcount == 0:
                return None
    return {'user_id': user_id, 'status': 'deleted'}