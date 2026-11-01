from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/xss")
def search():
    query = request.args.get("q")
    return render_template("xss.html", query=query)

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    print(username)
    print(password)
    return render_template("login.html")

app.run()

# https://wiki.python.org/python/archive/EscapingHtml.html

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
}

def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)