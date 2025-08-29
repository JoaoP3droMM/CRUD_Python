from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_users, delete_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Nome e email são obrigatórios'}), 400

    user = create_user(data)
    return jsonify(user.to_dict()), 201

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify([u.to_dict() for u in users])

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user = delete_user(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    return jsonify({'message': 'Usuário deletado com sucesso'})