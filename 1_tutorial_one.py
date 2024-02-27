from flask import Flask, render_template, url_for, redirect
# This line of code is used to get the flask as module to the file and hence it will be used in the file below

app = Flask(__name__)
# Here we have created the instance of the flask file which will be invoked after of give it a parameter as __name__ which is declared as __main__ in further calls of the functions


@app.route("/")
# app.route() is a function which is used to give the url to the function so that it will be used in the opening of the site
# Here / means that the route is defined for the home page or the entry page of the site and hence they will be used for the further processes

def home():
    return "Hello! this is the home page <h1>Hello<h1>"

# after the url of the method is set as per the app.route then the function which is defined below it has to be called
# Here in our case we have called the function home and hence the string which is defined there is also returned here

@app.route("/about")
def about_page():
    return "This is the about page and hence we can give information about us in the about page and hence this page has to have all the information about us and our site"

# app.route("/<get_name>")
# def greet_name(get_name):
#     return f"Hello Hello {get_name} it is pleasing to have you on board"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

# This the special use case of the app.route method where we can give name of the variable inside the <> and hence whatever will be the string at that position it can be given as input to function and hence it will be used later for the rendering into html page

@app.route("/my_admin")
def admin_page():
    return "This is the admin page and we can make it access only when we want to after adding certain conditions"
# this is the function which is used to get the admin page from other method as we can get the method to be called from another method
# There is a module in the flask which is called as redirect it takes the url as input
# Here to give url we have used the url for method which passed the url of the method which is given as input there

@app.route("/admin")
def get_admin():
    return redirect(url_for("admin_page"))
# This is where we have redirected the admin route to myadmin
# We can add another one or two conditions here so that we will be able to get logging into the admin page only we have the access to enter the admin page


if __name__ == '__main__':
    app.run()