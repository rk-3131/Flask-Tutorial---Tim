from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", content="Radhakrushna Mahadik")

@app.route("/second_render")
def second_page():
    return render_template("second.html", list_file = ["RK", "Piyush", "Saurabh", "Avi", "Sush", "Nachiket"], list_city=["Mumbai", "Pune", "Delhi", "Mathura", "Kashi", "Ayodhya"])



if (__name__ == "__main__"):
    app.run(debug=True)