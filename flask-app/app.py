from flask import Flask
 # You’re importing the Flask class from the flask package.
 # Flask is a micro web framework — meaning it’s lightweight but powerful enough to build both small and large apps.
 # Flask is a lightweight Python web framework used to build web apps and APIs.

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Shubhra! Welcome to your first Flask App 🚀"

if __name__ == "__main__":
    # debug=True is fine locally while learning; remove or set False in production
    app.run(host="0.0.0.0", port=5000, debug=True)

 # When you call app.run() without specifying a port, Flask listens on port 5000 by default.
 # Default run shows in the console: * Running on http://127.0.0.1:5000
 # app.run() starts Flask’s built-in dev server (easy for local testing).