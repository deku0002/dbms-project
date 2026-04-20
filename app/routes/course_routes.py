from flask import Blueprint, request, jsonify
from app.models import db, Course

course_bp = Blueprint('course_bp', __name__)

# GET all courses
@course_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([
        {
            "course_id": c.course_id,
            "title": c.title,
            "description": c.description,
            "instructor_id": c.instructor_id
        } for c in courses
    ])


# POST create course
@course_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.json

    new_course = Course(
        title=data.get('title'),
        description=data.get('description'),
        instructor_id=data.get('instructor_id')
    )

    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully"}), 201


# PUT update course
@course_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.json

    course.title = data.get('title', course.title)
    course.description = data.get('description', course.description)
    course.instructor_id = data.get('instructor_id', course.instructor_id)

    db.session.commit()

    return jsonify({"message": "Course updated successfully"})


# DELETE course
@course_bp.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"})