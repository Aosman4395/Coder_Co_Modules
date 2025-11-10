
FROM python:3.8-slim 

WORKDIR /app

# Copy requirement list
COPY . .

# Install required packages into a separate directory
RUN pip install flask redis

# Expose your Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app-challenge.py"]
