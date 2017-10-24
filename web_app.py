from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('narrow/index.html')

@app.route('/index.html')
def home():
    return render_template('narrow/index.html')

@app.route('/about.html')
def about():
    return render_template('narrow/about.html')

@app.route('/blog.html')
def blog():
    return render_template('narrow/blog.html')

if __name__ == '__main__':
    #HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    #PORT = int(os.environ.get('PORT', 5000))
    #app.run(host=HOST, port=PORT)
    app.run()
