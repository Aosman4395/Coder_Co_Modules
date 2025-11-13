# Flask + MySQL Docker App

This is the **first Docker project** I created as a beginner. It is a very basic Flask application connected to a MySQL database, designed to help me understand the fundamentals of containerization, multi-container applications, and Docker workflow.

---

## Overview

- A simple Flask web application that displays a **welcome message** and the **MySQL version**.  
- Integrated with **MySQL** running in a separate Docker container.  
- Demonstrates the **core Docker concepts** for beginners: linking containers, exposing ports, and building multi-service applications.

---

## What I Learned

This first app was a great starting point for learning Docker and related technologies:

1. **Basic Project Structure**
   - Learned the importance of having **three key files**: `app.py`, `Dockerfile`, and `docker-compose.yml`.  
   - Understood how these files work together to define, build, and run a multi-container application.

2. **Flask Basics**
   - Set up a simple Flask web server and created routes.  
   - Integrated Flask with a MySQL database using Python’s `MySQLdb` library.

3. **MySQL in Docker**
   - Created a MySQL container and connected it to Flask.  
   - Learned how to pass credentials, link containers, and access database services from the app container.

4. **Port Management**
   - Learned how to map container ports to local machine ports.  
   - Ensured both the Flask app and MySQL database could communicate without conflicts.

---

## 🐳 How to Build and Run

1. **Build and start the containers:**

> `docker-compose up --build`

2. **Access the Flask app in your browser:**

http://localhost:5000

3. **Stop the containers when done:**

> `docker-compose down`