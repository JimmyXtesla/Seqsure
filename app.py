#Import the necessary libraries 

import flask 
from flask import Flask, render_template
from flask_sqlachelmy import QSLAlchemy

app = Flask(__name__) #initializing the app
db = SQLAlchemy(app)

class files(db.model):
	name = db.Column(nullable=False,)




@app.route('/')
def index():
	user_name = "Belson"
	return render_template("dashboard.html", user_name=user_name)

@app.route('/notifications')
def notifications():
	return render_template("notifications.html")

if __name__ == "__main":
	app.run(debug=True)


