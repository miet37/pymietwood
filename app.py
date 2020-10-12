from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><p><h1>Janusz ... to dla Ciebie,</h1></p><p>Hello, World! - pierwsza app na Azure</p></body></html>"
