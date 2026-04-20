from app.extensions import db


# ---------------- USERS ----------------
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)


# ---------------- COURSES ----------------
class Course(db.Model):
    __tablename__ = 'courses'

    course_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    instructor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


# ---------------- ENROLLMENTS ----------------
class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    enroll_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
    enroll_date = db.Column(db.String(20))


# ---------------- ASSIGNMENTS ----------------
class Assignment(db.Model):
    __tablename__ = 'assignments'

    assignment_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(20))


# ---------------- SUBMISSIONS ----------------
class Submission(db.Model):
    __tablename__ = 'submissions'

    submission_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assignment_id'))
    submission_date = db.Column(db.String(20))
    status = db.Column(db.String(20))


# ---------------- GRADES ----------------
class Grade(db.Model):
    __tablename__ = 'grades'

    grade_id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submissions.submission_id'))
    marks = db.Column(db.Integer)
    feedback = db.Column(db.String(200))