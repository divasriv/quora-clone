# 📝 Quora Clone
![License](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue.svg)

A minimal Quora-inspired Q&A platform built with Django.

## ⚙️ Features

- 🔐 User registration and login (with Django's auth system)
- ❓ Post a question
- 💬 View questions and answers
- ✍️ Answer questions
- ❤️ Like and unlike answers
- 🧾 Bootstrap-styled UI for basic usability

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone git@github.com:divasriv/quora-clone.git
   cd quora-clone
   ```
2. **Create a virtual environment**
    ``` bash
    python -m venv venv
    source venv/bin/activate  # on Windows: venv\Scripts\activate
    ```
3. **Install dependencies**
    ``` bash
    pip install -r requirements.txt
    ```
4. **Run migrations**
    ``` bash
    python manage.py migrate
    ```
5. **Create a superuser (optional)**
    ``` bash
    python manage.py createsuperuser
    ```
6.  **Run the development server**

    ``` bash
    python manage.py runserver
    ```

## 🧪 Tech Stack
- Python
- Django
- SQLite
- Bootstrap 5 (CDN)

## Notes
> ⚠️ **Note:** The commit history has been rebased and cleaned for readability, so the original commit timestamps may not reflect the actual development timeline.

## 🧑‍💻 Author
👋 Hi, I'm Diva — a backend developer who enjoys building clean, functional web applications with Django and Python.
This project is a minimalist Quora-inspired Q&A platform built to demonstrate backend design, authentication, and CRUD functionality using Django.
Feel free to fork this repo, contribute, or reach out for collaboration!
