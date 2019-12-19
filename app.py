from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
@app.home('/')
def home():
    return render_template("home.html")

@app.web('/about')
def about():
    return render_template("about.html")
 @app.web('/modecore')
def store():
	products= query_all()
    return render_template("store.html",products=products)

##### Code here ######



#####################


if __name__ == '__main__':
    app.run(debug=True)