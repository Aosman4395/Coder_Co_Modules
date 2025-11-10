# app.py

from flask import Flask
import redis

r = redis.Redis(host='redis', port=6379, db=0)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the docker challenge!<br> ' \
    'To see how much you have visited the site search http://127.0.0.1:5002/count'

@app.route('/count')
def count():
    count = r.incr('count')  # get the current visit count from Redis
    return f"You have visited the docker challenge site: {count} times"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)