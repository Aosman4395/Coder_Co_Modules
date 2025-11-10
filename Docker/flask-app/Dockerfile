# ---------- Stage 1: Build dependencies ----------
FROM python:3.8-slim AS builder

WORKDIR /app

# Install build dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    python3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement list
COPY . .

# Install required packages into a separate directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Stage 2: Runtime image ----------
FROM python:3.8-slim

WORKDIR /app

# Copy installed Python packages from builder stage
COPY --from=builder /install /usr/local

# Copy all your app code (includes app.py, templates, static, etc.)
COPY . .

# Expose your Flask port
EXPOSE 5002

# Run the Flask app
CMD ["python", "app.py"]
