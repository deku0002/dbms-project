from flask import Blueprint, request, jsonify
from app.models import db, Grade

grade_bp = Blueprint('grade_bp', __name__)

# GET all grades
@grade_bp.route('/grades', methods=['GET'])
def get_grades():
    grades = Grade.query.all()
    return jsonify([
        {
            "grade_id": g.grade_id,
            "submission_id": g.submission_id,
            "marks": g.marks,
            "feedback": g.feedback
        } for g in grades
    ])


# POST create grade
@grade_bp.route('/grades', methods=['POST'])
def create_grade():
    data = request.json

    new_grade = Grade(
        submission_id=data.get('submission_id'),
        marks=data.get('marks'),
        feedback=data.get('feedback')
    )

    db.session.add(new_grade)
    db.session.commit()

    return jsonify({"message": "Grade created successfully"}), 201


# PUT update grade
@grade_bp.route('/grades/<int:grade_id>', methods=['PUT'])
def update_grade(grade_id):
    grade = Grade.query.get_or_404(grade_id)
    data = request.json

    grade.submission_id = data.get('submission_id', grade.submission_id)
    grade.marks = data.get('marks', grade.marks)
    grade.feedback = data.get('feedback', grade.feedback)

    db.session.commit()

    return jsonify({"message": "Grade updated successfully"})


# DELETE grade
@grade_bp.route('/grades/<int:grade_id>', methods=['DELETE'])
def delete_grade(grade_id):
    grade = Grade.query.get_or_404(grade_id)

    db.session.delete(grade)
    db.session.commit()

    return jsonify({"message": "Grade deleted successfully"})