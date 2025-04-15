# Report-Gen-PyDjango

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0%2B-brightgreen)](https://www.djangoproject.com/)
[![Build Status](https://img.shields.io/badge/Build-Passing-success)](https://github.com/nothingmakes-sense/report-gen-pydjango/actions)

A lightweight Django-based web application for generating customizable reports. This repository features a robust back end written in Python and Django, with a dynamic front end powered by JavaScript, CSS, and HTML.

---

## 🚀 Features

- **Dynamic Report Generation:** Easily create and manage reports with customizable templates.
- **Responsive UI:** A beautiful, mobile-friendly user interface built with modern web technologies.
- **Secure & Scalable:** Built on Django, ensuring robust security and scalability for production use.
- **Dockerized Deployment:** Simplified containerized deployment using Docker.

---

## 🛠️ Technologies Used

- **Back End:** Django (Python)
- **Front End:** JavaScript, CSS, HTML
- **Containerization:** Docker
- **Other Tools:** SQLite (default database)

---

## 📦 Installation Instructions

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.8 or higher
- Node.js and npm (for front-end dependencies)
- Docker (optional, for containerized deployment)

### Step 1: Clone the Repository

```bash
git clone https://github.com/nothingmakes-sense/report-gen-pydjango.git
cd report-gen-pydjango
```

### Step 2: Set Up a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### Step 3: Install Back-End Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Front-End Dependencies

```bash
npm install
```

### Step 5: Apply Migrations

```bash
python manage.py migrate
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the application in action.

---

## 🐳 Docker Usage (Optional)

To run the application in a Docker container:

### Build the Docker Image

```bash
docker build -t report-gen-pydjango .
```

### Run the Docker Container

```bash
docker run -p 8000:8000 report-gen-pydjango
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## 🌐 Demo

A live demo will be available soon.

---

## 📧 Contact
