# Redis Visit Counter Docker App

This is the **second Docker project** I created as part of the Docker module. It is a Flask application integrated with Redis to demonstrate **multi-container orchestration**, container communication, and simple data persistence.

---

## Overview

- A Flask app with:  
  - A **welcome page**  
  - A **visit count page** that increments every time a user visits  
- Uses **Redis** as a key-value store to track the number of visits.  
- Demonstrates **multi-container setup** using Docker Compose, connecting a web app container to a Redis container.  

---

## What I Learned

This project built on my first app and introduced new Docker concepts:

1. **Redis Integration**
   - Learned how to connect a Flask app to a Redis container.  
   - Used Redis to **store and increment a simple counter**, demonstrating persistent state across container restarts.

2. **Multi-Container Applications**
   - Learned how to run **multiple services together** using `docker-compose.yml`.  
   - Used `depends_on` to ensure the Flask app waits for Redis to be ready.  
   - Explored container networking so containers can communicate via their service names (`redis`).

3. **Flask Enhancements**
   - Created multiple routes (`/` and `/count`) to separate functionality.  
   - Dynamically rendered visit counts using Redis data.

4. **Port Management**
   - Learned to map container ports to local machine ports to avoid conflicts with other apps.  
   - Managed traffic so multiple apps could run independently on different ports.

5. **Incremental Learning**
   - This app helped me understand **how to link services in Docker** and use Redis as a lightweight, in-memory database for real-time data.

---

## 🐳 How to Build and Run

1. **Build and start the containers:**

> `docker-compose up --build`

2. **Access the Flask app in your browser:**

http://localhost:5000

3. **Stop the containers when done:**

> `docker-compose down`

