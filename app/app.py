from flask import Flask, request, render_template
from src.predict import predict_job

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["job"]
        result = predict_job(text)
    return render_template("index.html", result=result)

app.run(debug=True)
