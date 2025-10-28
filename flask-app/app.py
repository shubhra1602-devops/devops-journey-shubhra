from flask import Flask
 # You’re importing the Flask class from the flask package.
 # Flask is a micro web framework — meaning it’s lightweight but powerful enough to build both small and large apps.

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Shubhra! Welcome to your first Flask App 🚀"

if __name__ == "__main__":
    # debug=True is fine locally while learning; remove or set False in production
    app.run(host="0.0.0.0", port=5000, debug=True)
