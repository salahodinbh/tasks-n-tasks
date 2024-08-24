from flask import jsonify, request, Blueprint, send_from_directory
from flask_cors import CORS, cross_origin
from taskapi.models import db, Task
from datetime import datetime

api = Blueprint('taskapi', __name__)
CORS(api)

tasks = []
completedTasks = []

'''
@app.route('/', methods=['GET'])
def hello():
    return 'Hello from Flask! I hate this'
'''

@api.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@api.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@api.route('/completedtasks', methods=['GET'])
def list_completed_tasks():
    completed_tasks = Task.query.filter_by(completed=True).all()
    return jsonify([task.to_dict() for task in completed_tasks])

@api.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'The "name" field is required.'}), 400

    task = Task(name=data['name'])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@api.route('/tasks/<int:id>', methods=['POST'])
def complete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    task.completed = True
    task.completion_date = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Task completed successfully'})

@api.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

# Should've been set to main, but due to interferences with other apps/variables it's set to app.
#if app.name == 'app':
#    app.run(debug=True)