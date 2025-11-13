# Quran Ayah Docker App

This is the **third and most advanced Docker project** I created, representing my initiative to go beyond the module requirements. Unlike the previous apps, this project combines Flask, Redis, and dynamic content in **a single Python file** — no separate HTML templates — to create a **custom, interactive Quran Ayah web app**.

---

## Overview

- A Flask web application with:  
  - A visually appealing **welcome page** with background image and styled text embedded in the Python file  
  - A **daily Ayah page** that displays a random Quran verse in both Arabic and English  
  - A **visit counter** powered by Redis to track how many Ayahs a user has read  
- All the HTML and CSS is **directly in the Python file**, showing how dynamic content can be served without separate templates.  
- Uses a **Dockerfile** to containerize the Flask app and a **Docker Compose YAML file** to orchestrate multiple services (Flask + Redis).  
- Demonstrates **multi-container orchestration**, networking, and port management with Docker Compose.

---

## What I Learned

This project allowed me to **take initiative** and apply everything I learned from the previous Docker exercises:

1. **Single-File Flask Applications**
   - Embedded **HTML and CSS directly in Python routes** for dynamic content.  
   - Styled pages dynamically, including background images, text formatting, and links.

2. **Redis for Stateful Applications**
   - Used Redis to track user interactions and store counters.  
   - Built on knowledge from the Redis Visit Counter app to handle **persistent state** across container restarts.

3. **Dynamic Content**
   - Implemented random selection of Quran verses each time the `/ayah` route is visited.  
   - Combined Arabic and English text for user-friendly display.

4. **Docker & Docker Compose**
   - Created a **Dockerfile** to containerize the Flask app.  
   - Used a **Docker Compose YAML file** to run multiple services (Flask + Redis).  
   - Practiced **port management**, networking, and linking containers efficiently.

5. **Initiative & Problem Solving**
   - Designed a more advanced project **from scratch**, going beyond the basic exercises.  
   - Demonstrates the ability to combine multiple skills — Python, Flask, Redis, HTML/CSS, and Docker — into a **cohesive, interactive application**.

---

## 🐳 How to Build and Run

1. **Build and start the containers:**

> `docker-compose up --build`

2. **Access the Flask app in your browser:**

http://localhost:5000

3. **Stop the containers when done:**

> `docker-compose down`


