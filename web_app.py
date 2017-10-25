from flask import Flask, request
from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('narrow/index.html')

@app.route('/goals/')
def goals():
    return render_template('narrow/goals.html')

@app.route('/blog/')
def blog():
    return render_template('narrow/blog.html')

@app.route('/system/')
def system():
    return render_template('narrow/system.html')

@app.route('/contact/')
def contact():
    return render_template('narrow/contact.html')

@app.route('/process/')
def process():
    return render_template('narrow/process.html')

if __name__ == '__main__':
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host=HOST, port=PORT)
    #app.run()
