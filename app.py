# app.py - Simple Flask Web App
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
return "Hello, Azure PaaS! 🚀 - Student Web App"
if __name__ == '__main__':
app.run()
