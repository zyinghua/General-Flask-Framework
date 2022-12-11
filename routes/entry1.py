from flask import Blueprint, jsonify, request
from models import *
from database import db_session

entry1 = Blueprint('entry1', __name__)


@entry1.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])  # define HTTP endpoint & methods for this function
def index():
    """
    define your REST-ful logic here...
    e.g.: Data processing, Database manipulations...
    """
    return "API ENTRY POINT 1"


"""------------------------------------------------"""
"""Below are simple examples of doing database CRUD"""
"""------------------------------------------------"""


@entry1.route('/getAllUsers', methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(users)


@entry1.route('/getUserByEmail/<email>', methods=["GET"])
def get_user_by_email(email):
    u = User.query.filter_by(user_email=email).first()

    return jsonify(u) if u else {}


@entry1.route('/insertUser', methods=["POST"])
def insert_user():
    data = request.form
    username = data.get("username")
    email = data.get("email")

    u = User(user_name=username, user_email=email)

    db_session.add(u)
    db_session.commit()

    return jsonify(u)


@entry1.route('/deleteUserByEmail/<email>', methods=["DELETE"])
def delete_user_by_email(email):
    user_delete = db_session.query(User).get(user_email=email)

    if user_delete:
        db_session.delete(user_delete)

    return jsonify(user_delete)


@entry1.route('/updateUser', methods=['PUT'])
def update():
    # get the request form data with the updated attributes
    data = request.form
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({"status": "error", "message": "Missing user_id"})

    user_update = db_session.query(User).get(user_id)  # get a pointer to the user object for update

    if user_update is None:
        return jsonify({"status": "error", "message": "User Not Found"})

    username = data.get('username')
    email = data.get('email')

    if username is not None:
        user_update.user_username = username
    if email is not None:
        user_update.user_email = email

    db_session.commit()
    return jsonify(user_update)
