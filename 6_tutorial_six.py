from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        email = request.form["em"]
        name = request.form["nm"]
        return redirect(url_for("get_info", name=name, email=email))
    else:
        return render_template("login.html")


@app.route("/info")
def get_info():
    name = request.args.get("name")
    email = request.args.get("email")
    return render_template("email_name.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)