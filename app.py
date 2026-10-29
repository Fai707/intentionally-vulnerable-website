from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/xss")
def index():
    query = request.args.get("q")
    return render_template("xss.html", query=query)

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