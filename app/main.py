from flask import Flask, render_template, stream_with_context, Response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='HOME PAGE')

#@app.route('/docs')
#def docs():
#    return render_template('index.html', title='DOCS')

@app.route('/about')
def about():
    """def generate():
        for i in list("Sumagna Das"):
            yield i
            for i in range(0, int(20000000 * 0.1)):
                pass
    return Response(stream_with_context(generate()))"""
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
