from flask_restful import abort, Resource
from flask import jsonify
from .reqparse_jobs import parser
from . import db_session
from .jobs import Jobs
from datetime import datetime


def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify({
            'job':
                jobs.to_dict(only=(
                    'id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'category'))
        })

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({
            'jobs':
                [item.to_dict(only=(
                    'id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'category'))
                    for item in jobs]
        })

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.fromisoformat(args['start_date']),
            end_date=datetime.fromisoformat(args['end_date']),
            is_finished=bool(args['is_finished']),
            team_leader=args['team_leader'],
            category=args['category']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})
