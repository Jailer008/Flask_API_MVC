from flask import Blueprint, request, jsonify
from app.services.user_service import handle_get_user, handle_save_user, handle_update_user, handle_delete_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        result = handle_get_user(user_id)
        if result:
            return jsonify({"status": "ok", "user_name": result[1]}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

    elif request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        result = handle_save_user(user_id, user_name)
        if len(result) > 0:
            print(result)
            return jsonify({"status": "ok", "user_added": result}), 200
        else:
            return jsonify({"status": "error", "reason": "id already exists"}), 500

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        result = handle_update_user(user_id, user_name)
        if result:
            return jsonify({"status": "ok", "user_update": result}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

    elif request.method == 'DELETE':
        result = handle_delete_user(user_id)
        if result:
            return jsonify({"status": "ok", "user_dalete": result}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

@user_bp.route('/get_user_data/<user_id>', methods=['GET'])
def get_data(user_id):
    if request.method == 'GET':
        result = handle_get_user(user_id)
        if result:
            return jsonify({"status": "ok", "data": result}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

