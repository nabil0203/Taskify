# 📝 Taskify – To-Do Web Application

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


### Taskify is a full-stack **Django-based To-Do web application** built using **Django** and **Bootstrap**.  
### It allows users to manage their daily tasks with authentication, task filtering, and a clean UI.
### The project demonstrates strong fundamentals in **CRUD operations, authentication, relational database design, and MVC architecture**,


---


### 🔗 Live Demo (Deployed)

#### ➡️ See Taskify in action: https://taskify-cq2h.onrender.com/


---

## 🚀 Key Features

### 🔐 Authentication
- User Registration
- User Login & Logout
- Profile Update
- Password Change

### ✅ Task Management (CRUD)
- Create new tasks with:
  - Title
  - Description
  - Due Date
  - Due Time
- Update existing tasks
- View task details

### 📂 Task Viewing & Filtering
- View all tasks
- Filter tasks by status:
  - ✅ Completed Tasks
  - ⏳ Pending / Remaining Tasks

---

## 🧠 System Design Overview

- **Architecture:** Django MVT (Model–View–Template)
- **Authentication:** Django Built-in Auth
- **Database Design:** Relational (One-to-Many)
- **UI:** Responsive Bootstrap-based interface


---


## 🛠️ Tech Stack
- **Programming Language:** Python
- **Backend Framework:** Django
- **Frontend:** HTML5, Bootstrap
- **Database:** SQLite3
- **Version Control:** Git & GitHub

---


## 🏗️ Project Structure

```
taskify/
├── taskify/                 # Project configuration (settings, urls)
├── task_app/                # Main application logic
│   ├── migrations/          # Database migration files
│   ├── templates/           # App-specific HTML (login, task_list, etc.)
│   ├── models.py            # Task & User logic
│   ├── views.py             # Request handling
│   ├── forms.py             # Django Forms for Tasks/Profiles
│   └── urls.py              # App routing
├── templates/               # Global templates (base.html)
├── db.sqlite3               # SQLite Database
├── manage.py                # Django command-line utility
└── requirements.txt         # Project dependencies
```


---


## 🧩 Models

### 1️⃣ User Model
- Uses Django’s built-in `User` model
- Handles authentication and authorization


### 2️⃣ Task Model
- Represents individual tasks created by users.


#### Relationship:
- **One-to-Many**
  - `1 User` ➝ `Multiple Tasks`


---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/taskify.git
cd taskify
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate             # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```


5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run the server**
```bash
python manage.py runserver
```

7. **Open browser and visit:**
```bash
http://127.0.0.1:8000/
```

---


## 📌 Future Improvements
- Task priority system        
- Search functionality        
- Email reminders     
- REST API support


---

## 🤝 Contributing
- Contributions, issues, and feature requests are welcome!
- Feel free to fork this repo and submit pull requests.

--- 

## 📜 License
- This project is open-source and available under the MIT License
