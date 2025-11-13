# 🐳 Docker Module Projects

This repository showcases my hands-on projects from the **Docker module**, demonstrating my understanding of containerization, multi-container applications, and deploying applications using Docker and Docker Compose.  

While each project includes its own detailed README, this main repository gives an overview of the three applications I created as part of this module.

---

## Projects Overview

### 1. Flask + MySQL App
- A simple Flask web application displaying a **welcome message**.  
- Integrated **MySQL** as the database backend.  
- Demonstrates how to **containerize a web application** and link it to a database service using Docker.

### 2. Redis Visit Counter App
- A Flask app with:
  - A **welcome page**
  - A **visit count page** that increments each time the page is visited.  
- Uses **Redis** as a key-value store to track visits.  
- Shows **multi-container setup** with Docker Compose and inter-container communication.

### 3. Quran Ayah App
- A **more advanced project** I created on my own initiative.  
- Displays **random Quran ayahs** in Arabic and English every time the page is visited.  
- Tracks the number of ayahs read using **Redis**.  
- Combines the skills learned from the previous apps into a **single, full-stack, containerized application**.

---

## 🐳 Docker Skills Demonstrated

Through these projects, I applied the following Docker skills:

- **Dockerfiles:** Created separate Dockerfiles for each application to define the runtime environment.  
- **Docker Compose:** Managed multi-container applications (web + database/Redis) for easy orchestration.  
- **Docker Hub:** Built images locally and pushed them to Docker Hub for versioning and sharing.  
- **Container Networking:** Linked multiple services (Flask apps, MySQL, Redis) together in isolated networks.  
- **Volume Management:** Persisted database data across container restarts using Docker volumes.  

---
