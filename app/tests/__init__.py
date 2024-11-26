from app.db import get_db_connection
from app.config import Config
from pypika import Table, Query

def get_config():
    connection = get_db_connection()
    config_data = {}
    table = Table(Config.DB_NAME + ".config")

    try:
        with (connection.cursor() as cursor):
            query = Query.from_(table).select(table.id, table.api_gateway_url, table.browser, table.default_user_name)
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                config_data = {
                    "id": result[0],
                    "api_gateway_url": result[1],
                    "browser": result[2],
                    "default_user_name": result[3]
                }
    finally:
        connection.close()

    return config_data