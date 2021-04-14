# Add dependencies
from flask import Flask, jsonify

# Set up Flask
app = Flask (__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
