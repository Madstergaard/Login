from flask import Flask, render_template, request, session, url_for# Capital Flask is a subset of the module flask
import hashlib

app = Flask(__name__)
app.secret_key = '%t\x15\x94\x00\x11g\x98\x13\xcexI].\xc3F\xdaM\xfeB\x9ay\x11\xc7\x81lG:\xc8\xd8y\x8a'


# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/") 
@app.route("/home/", methods = ["POST"])

def welcome():
	success = ""
    	return render_template('login.html', footer = success)
    
	
# Register page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/register/") 

def login():
	with open("passwords.txt" , "a") as PassWordFile:
		PassWordFile.write("Testing 123\n")          
	return render_template('login.html', footer = "You have created a new account!")
   

 # Login page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/login/") 

def login():
    success = ""
    filled_form = request.form # if success == "":
    PasswordFile.write(filled_form["username"] + " " + filled_form["password"] + "\n")         
	success = "You have created a new account!"
	return render_template('login.html', footer = success)
    
	with open("passwords.txt", "a") as PassWordFile
    for line in PasswordFile.readlines():
    	account = line.split()
    	if account[0] == filled_form["username"]:
    		if account[1] == filled_form["password"]:
    			success = "You have successfully logged in!"
    			return render_template('login.html', footer = success)
			else:
				success = "The password you submitted is incorrect."
				return render_template('login.html', footer = success)
	PasswordFile.close()
        



if __name__ == '__main__':
    app.debug = True
    app.run()

