from flask import Flask, render_template, stream_with_context, Response, request
app = Flask(__name__)

@app.route('/')
def index():
    location = request.args.get('location')
    if location == "home":
        return render_template('index.html', title='HOME PAGE', homePressed=True)
    else:
        return render_template('index.html', title='HOME PAGE')

#@app.route('/docs')
#def docs():
#    return render_template('index.html', title='DOCS')

"""@app.route("/stream")
def stream():
    def generate():
        yield "<link rel=\"stylesheet\" href=\"static/about.css\">\n<br><span class=\"name\">&gt;&nbsp&nbsp"#<span class=\"labels\">Name</span>\t"
        for i in list("Sumagna Das"):
            yield i
            for i in range(0, int(10000000 * 0.5)):
                pass
        yield "</span>"
    return Response(stream_with_context(generate()))"""

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
