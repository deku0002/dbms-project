# 🎓 EduNova – Smart E-Learning Management System

A modern, database-driven **E-Learning Management System (LMS)** built using **Flask, SQLAlchemy, and a dynamic frontend UI**.
This project demonstrates real-world implementation of **DBMS concepts, full-stack web development, and cloud deployment**.

---

## 🚀 Features

* 👤 User Management (Students & Instructors)
* 📚 Course Creation & Enrollment
* 📝 Assignment Management
* 📤 Submission Tracking
* 📊 Grade Management
* 🔄 Full CRUD Operations (Create, Read, Update, Delete)
* 🌐 REST API integration using Flask
* 🎨 Interactive Admin Dashboard (Console UI)
* ☁️ Ready for AWS EC2 + RDS Deployment

---

## 🏗️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Database:** SQLite (Development) → MySQL (AWS RDS)
* **ORM:** SQLAlchemy
* **Deployment:** AWS EC2
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
edunova-lms/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   ├── config.py
│   └── extensions.py
│
├── static/
│   └── elms.html
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/edunova-lms.git
cd edunova-lms
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python run.py
```

App will run on:

```
http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

### Users

* `GET /api/users`
* `POST /api/users`
* `PUT /api/users/<id>`
* `DELETE /api/users/<id>`

### Courses

* `GET /api/courses`
* `POST /api/courses`
* `PUT /api/courses/<id>`
* `DELETE /api/courses/<id>`

### Enrollments

* `GET /api/enrollments`
* `POST /api/enrollments`
* `DELETE /api/enrollments/<id>`

### Assignments, Submissions, Grades

* Similar REST-based CRUD endpoints

---

## ☁️ Deployment (AWS)

* Launch an EC2 instance (Ubuntu)
* Install Python & required dependencies
* Run application using **Gunicorn**
* Configure security groups (open ports 5000/80)
* Connect backend to **AWS RDS (MySQL)**

---

## 🧠 Concepts Covered

* Relational Database Design (ER Model)
* SQL (DDL, DML, Joins, Views)
* REST API Development
* 3-Tier Architecture:

  * UI Layer
  * Application Layer
  * Database Layer
* CRUD Operations
* Cloud Deployment

---

## 📸 Screenshots

*Add screenshots of your frontend here to enhance presentation*

---

## 👨‍💻 Team & Contributions

This project was submitted as a team effort:

* Devansh Sharma
* Ayush Sharma
* Shivam Bhatia

### 🔹 Contribution Breakdown

* **Devansh Sharma**

  * Designed and developed the complete **frontend UI (EduNova Console)**
  * Built the **Flask backend and REST API integration**
  * Connected frontend with backend and handled **full system workflow**
  * Prepared the project for **deployment (AWS EC2 + RDS)**

* **Ayush Sharma & Shivam Bhatia**

  * Contributed to **project documentation and report preparation**
  * Assisted with **SQL queries and database design support**

---

> The core development and implementation of the working system were primarily carried out by Devansh Sharma, with supporting contributions from the team in documentation and database-related tasks.

---

## 🎯 Future Scope

* 🔐 Authentication & Authorization (JWT)
* 📊 Analytics Dashboard
* 📩 Notification System
* 📱 Mobile App Integration
* 🎥 Live Classes Support

---

## 📜 License

This project is for **educational purposes only**.

---

## ⭐ Show Some Love

If you found this project useful, consider giving it a ⭐ on GitHub!
