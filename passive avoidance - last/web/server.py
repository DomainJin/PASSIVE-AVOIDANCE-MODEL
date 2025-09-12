from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/get")
def hello_world():
    startTime = request.args.get("startTime")
    endTime = request.args.get("endTime")
    print(startTime)
    print(endTime)
    
    return jsonify("passive-avoidance-a.jpg")

if __name__ == "__main__":
    app.run(debug=True)

