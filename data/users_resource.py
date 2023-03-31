from flask_restful import abort, Resource
from flask import jsonify
from .reqparse_user import parser
from . import db_session
from .users import User


def abort_if_users_not_found(uid):
    session = db_session.create_session()
    users = session.query(User).get(uid)
    if not users:
        abort(404, message=f"User {uid} not found")


class UsersResource(Resource):
    def get(self, uid):
        abort_if_users_not_found(uid)
        session = db_session.create_session()
        users = session.query(User).get(uid)
        return jsonify({
            'user':
                users.to_dict(only=(
                    'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password'))
        })

    def delete(self, uid):
        abort_if_users_not_found(uid)
        session = db_session.create_session()
        users = session.query(User).get(uid)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            'users':
                [item.to_dict(only=(
                    'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password'))
                    for item in users]
        })

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
