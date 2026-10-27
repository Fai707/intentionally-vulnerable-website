from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/xss")
def index():
    query = request.args.get("q")
    return render_template("xss.html", query=query)

app.run()