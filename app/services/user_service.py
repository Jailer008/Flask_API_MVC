from app.db.db_queries import get_user, save_user, update_user, delete_user

def handle_get_user(user_id):
    return get_user(user_id)

def handle_save_user(user_id, user_name):
    return save_user(user_id, user_name)

def handle_update_user(user_id, user_name):
    return update_user(user_id, user_name)

def handle_delete_user(user_id):
    return delete_user(user_id)