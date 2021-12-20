from flask import Flask, render_template
app = Flask(__name__,
            static_folder='src/static/',
            template_folder='src/templates/')


@app.route("/")
def home():
    return render_template("index.html")