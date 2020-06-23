from flask import Flask, render_template, stream_with_context, Response, request
from datetime import date, timedelta

birthday = date(2006, 1, 11)
today = date.today()

age = (today - birthday)/ timedelta(365)
age = "14+" if age > int(age) else "14"
app = Flask(__name__)

@app.route('/')
def home():
    location = request.args.get('location')
    if location == "home":
        return render_template('index.html', title='HOME PAGE', homePressed=True)
    else:
        return render_template('index.html', title='HOME PAGE')

@app.route('/about')
def about():
    return render_template("about.html", age=age)

if __name__ == "__main__":
    app.run()
