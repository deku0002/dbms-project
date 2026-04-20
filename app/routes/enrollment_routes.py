from flask import Blueprint, request, jsonify
from app.models import db, Enrollment

enrollment_bp = Blueprint('enrollment_bp', __name__)

# GET all enrollments
@enrollment_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    enrollments = Enrollment.query.all()
    return jsonify([
        {
            "enroll_id": e.enroll_id,
            "user_id": e.user_id,
            "course_id": e.course_id,
            "enroll_date": e.enroll_date
        } for e in enrollments
    ])


# POST create enrollment
@enrollment_bp.route('/enrollments', methods=['POST'])
def create_enrollment():
    data = request.json

    new_enrollment = Enrollment(
        user_id=data.get('user_id'),
        course_id=data.get('course_id'),
        enroll_date=data.get('enroll_date')
    )

    db.session.add(new_enrollment)
    db.session.commit()

    return jsonify({"message": "Enrollment created successfully"}), 201


# DELETE enrollment
@enrollment_bp.route('/enrollments/<int:enroll_id>', methods=['DELETE'])
def delete_enrollment(enroll_id):
    enrollment = Enrollment.query.get_or_404(enroll_id)

    db.session.delete(enrollment)
    db.session.commit()

    return jsonify({"message": "Enrollment deleted successfully"})