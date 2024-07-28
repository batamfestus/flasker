from flask import Flask, render_template

# create a flask instancce
app = Flask(__name__)

fruits = ['orange', 'pear', 'mango', 'berry', 'black current']

# create a route decorator
@app.route("/")
def index():
    return render_template('index.html', fruit=fruits)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

############## CREATING CUSTOM ERROR PAGES
## Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
## Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500