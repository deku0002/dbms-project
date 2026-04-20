from flask import Blueprint, request, jsonify
from app.models import db, Submission

submission_bp = Blueprint('submission_bp', __name__)

# GET all submissions
@submission_bp.route('/submissions', methods=['GET'])
def get_submissions():
    submissions = Submission.query.all()
    return jsonify([
        {
            "submission_id": s.submission_id,
            "user_id": s.user_id,
            "assignment_id": s.assignment_id,
            "submission_date": s.submission_date,
            "status": s.status
        } for s in submissions
    ])


# POST create submission
@submission_bp.route('/submissions', methods=['POST'])
def create_submission():
    data = request.json

    new_submission = Submission(
        user_id=data.get('user_id'),
        assignment_id=data.get('assignment_id'),
        submission_date=data.get('submission_date'),
        status=data.get('status')
    )

    db.session.add(new_submission)
    db.session.commit()

    return jsonify({"message": "Submission created successfully"}), 201


# PUT update submission
@submission_bp.route('/submissions/<int:submission_id>', methods=['PUT'])
def update_submission(submission_id):
    submission = Submission.query.get_or_404(submission_id)
    data = request.json

    submission.user_id = data.get('user_id', submission.user_id)
    submission.assignment_id = data.get('assignment_id', submission.assignment_id)
    submission.submission_date = data.get('submission_date', submission.submission_date)
    submission.status = data.get('status', submission.status)

    db.session.commit()

    return jsonify({"message": "Submission updated successfully"})


# DELETE submission
@submission_bp.route('/submissions/<int:submission_id>', methods=['DELETE'])
def delete_submission(submission_id):
    submission = Submission.query.get_or_404(submission_id)

    db.session.delete(submission)
    db.session.commit()

    return jsonify({"message": "Submission deleted successfully"})