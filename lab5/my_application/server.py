from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Index page"
@app.route("/hello")
def hello():
    return "Hello World!"
@app.route("/user/paul")
def user():
    return "User paul"
@app.route("/post/80")
def post():
    return "Post 80"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
