from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

tasks = []
completedTasks = []

'''
@app.route('/', methods=['GET'])
def hello():
    return 'Hello from Flask! I hate this'
'''

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks)

@app.route('/completedtasks', methods=['GET'])
def list_completed_tasks():
    return jsonify(completedTasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.get_json()
    task = task.get('task','')
    tasks.append(task)
    return jsonify(task)

@app.route('/tasks/<int:index>', methods=['POST'])
def complete_task(index):
    completedTasks.append(tasks[index])
    delete_task(index)
    return jsonify({'message': 'Task completed successfully'})

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    try:
        tasks.pop(index)
        return jsonify({'message': 'Task deleted successfully'})
    except IndexError:
        return jsonify({'error': 'Task not found'}), 404

# Should've been set to main, but due to interferences with other apps/variables it's set to app.
if app.name == 'app':
    app.run(debug=True)