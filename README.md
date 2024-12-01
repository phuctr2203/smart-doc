# smart-doc
Smart Documents AI service


# Flask Clean Architecture Backend

This repository contains a Python Flask backend application structured using **Clean Architecture** principles. This architecture ensures separation of concerns, scalability, and maintainability.

---

## **Directory Structure**
The project is organized as follows:

Here’s the terminal prompt script to generate the folder and file structure for your Flask project following Clean Architecture principles, along with a README.md description template.

Terminal Commands
Run the following commands in the terminal to set up the structure:

bash
Copy code
# Create the main project directory
mkdir flask-clean-architecture
cd flask-clean-architecture

# Create main app folder
mkdir app
cd app

# Create subdirectories for Clean Architecture layers
mkdir controllers models repositories schemas services tests

# Create __init__.py files for each module
touch __init__.py
touch controllers/__init__.py
touch models/__init__.py
touch repositories/__init__.py
touch schemas/__init__.py
touch services/__init__.py
touch tests/__init__.py

# Create config and main entry point
cd ..
touch app.py
touch requirements.txt

# Create a migrations folder (for database migrations)
mkdir migrations

# Create README.md
touch README.md
README.md Description Template
Add the following content to the README.md file:

markdown
Copy code
# Flask Clean Architecture Backend

This repository contains a Python Flask backend application structured using **Clean Architecture** principles. This architecture ensures separation of concerns, scalability, and maintainability.

---

## **Directory Structure**
The project is organized as follows:

flask-clean-architecture/ ├── app/ # Main application code │ ├── init.py # Application factory │ ├── config.py # Configuration settings │ ├── controllers/ # Handles HTTP requests and routes │ ├── models/ # Database models (entities) │ ├── repositories/ # Data access and persistence logic │ ├── schemas/ # Data validation and serialization │ ├── services/ # Core business logic (use cases) │ ├── tests/ # Unit and integration tests ├── migrations/ # Database migrations ├── app.py # Entry point for the application ├── requirements.txt # Python dependencies └── README.md # Project documentation

---

## **Setup Instructions**

### 1. Setup Backend Environment

- cd backend
- python3 -m venv venv
- source venv/bin/activate or venv\Scripts\activate
- Install libraries: pip install -r requirements.txt

### 2. Setup Frontend Environent

- cd frontend
- npm install

## **How to run**

### 1. Backend
- cd backend
- python app.py

### 2. Frontend
- npm start