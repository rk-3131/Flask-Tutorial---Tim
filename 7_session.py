from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "Radhakrushna"
# This is the secrete key which has to be set just for the security concerns

@app.route("/")
def homePage():
    return render_template("new_inherited.html")

@app.route("/login", methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        name = request.form['nm']
        session["name"] = name
        # session stores the value in the form of key and value pair and hence it will be used for the purpose of later then to serve the same value on the same session
        # return redirect(url_for("logged_in", name = name))
        return redirect(url_for("new_logged_in"))
    else:
        return render_template("session_login.html")


@app.route("/user_name")
def new_logged_in():
    name = session["name"]
    # Now the value of the name has been recovered from the session and hence it is now accessible from any point in the same session
    return render_template("show_name.html", usr = name)


@app.route("/<name>")
def logged_in(name):
    return render_template("show_name.html", usr = name)



if __name__ == "__main__":
    app.run(debug=True)