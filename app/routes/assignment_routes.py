from flask import Blueprint, request, jsonify
from app.models import db, Assignment

assignment_bp = Blueprint('assignment_bp', __name__)

# GET all assignments
@assignment_bp.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = Assignment.query.all()
    return jsonify([
        {
            "assignment_id": a.assignment_id,
            "course_id": a.course_id,
            "title": a.title,
            "description": a.description,
            "due_date": a.due_date
        } for a in assignments
    ])


# POST create assignment
@assignment_bp.route('/assignments', methods=['POST'])
def create_assignment():
    data = request.json

    new_assignment = Assignment(
        course_id=data.get('course_id'),
        title=data.get('title'),
        description=data.get('description'),
        due_date=data.get('due_date')
    )

    db.session.add(new_assignment)
    db.session.commit()

    return jsonify({"message": "Assignment created successfully"}), 201


# PUT update assignment
@assignment_bp.route('/assignments/<int:assignment_id>', methods=['PUT'])
def update_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    data = request.json

    assignment.title = data.get('title', assignment.title)
    assignment.description = data.get('description', assignment.description)
    assignment.course_id = data.get('course_id', assignment.course_id)
    assignment.due_date = data.get('due_date', assignment.due_date)

    db.session.commit()

    return jsonify({"message": "Assignment updated successfully"})


# DELETE assignment
@assignment_bp.route('/assignments/<int:assignment_id>', methods=['DELETE'])
def delete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)

    db.session.delete(assignment)
    db.session.commit()

    return jsonify({"message": "Assignment deleted successfully"})