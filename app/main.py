from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>INDEX PAGE</h1>"

@app.route('/docs')
def docs():
    return render_template('index.html', title='DOCS')

@app.route('/about')
def about():
    return render_template('index.html', title='ABOUT')

if __name__ == "__main__":
    app.run()
