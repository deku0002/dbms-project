from flask import Blueprint, request, jsonify
from app.models import db, User

user_bp = Blueprint('user_bp', __name__)

# GET all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "user_id": u.user_id,
            "name": u.name,
            "email": u.email,
            "role": u.role
        } for u in users
    ])


# POST create user
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json

    new_user = User(
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password'),
        role=data.get('role')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


# PUT update user
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.role = data.get('role', user.role)

    db.session.commit()

    return jsonify({"message": "User updated successfully"})


# DELETE user
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"})