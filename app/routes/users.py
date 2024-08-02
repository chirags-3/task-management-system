from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    user = User(username=request.json['username'], password=request.json['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())

@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())

@users_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user.username = request.json.get('username', user.username)
    user.password = request.json.get('password', user.password)
    db.session.commit()
    return jsonify(user.to_dict())

@users_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})