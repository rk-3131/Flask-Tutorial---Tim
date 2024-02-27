from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("show_name", usr = user))
    else:
        return render_template("getName.html")

@app.route("/<usr>")
def show_name(usr):
    return render_template("show_name.html", usr = usr)

if __name__ == "__main__":
    app.run(debug=True)