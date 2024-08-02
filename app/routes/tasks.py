from flask import Blueprint, request, jsonify
from app import db
from app.models.task import Task

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    task = Task(title=request.json['title'], description=request.json['description'], status=request.json['status'], priority=request.json['priority'], due_date=request.json['due_date'])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict())

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.to_dict())

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task.title = request.json['title']
    task.description = request.json['description']
    task.status = request.json['status']
    task.priority = request.json['priority']
    task.due_date = request.json['due_date']
    db.session.commit()
    return jsonify(task.to_dict())

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})