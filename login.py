from flask import Flask, render_template, request # Capital Flask is a subset of the module flask
import hashlib

app = Flask(__name__)


# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/") 
@app.route("/home/", methods = ["POST"])

def welcome():
	success = ""
    	return render_template('login.html', footer = success)
    
	
# Register page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/register/") 

def login():
	open("passwords.txt" , "a").write("Testing 123\n")          
	return render_template('login.html', footer = "You have created a new account!")
   

    



if __name__ == '__main__':
    app.debug = True
    app.run()

