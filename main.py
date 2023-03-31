from flask import Flask
from flask_restful import Api
from data import db_session, users_resource, jobs_resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)
app.config['JSON_AS_ASCII'] = False


def main():
    db_session.global_init("db/mars_explorer.db")
    # для списка объектов
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')

    # для одного объекта
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:uid>')
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')

    # для одного объекта
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
    app.run()


if __name__ == '__main__':
    main()
