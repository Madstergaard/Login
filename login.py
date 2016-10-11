from flask import Flask, render_template, request, session, url_for, redirect# Capital Flask is a subset of the module flask
import hashlib, csv

app = Flask(__name__)
app.secret_key = '%t\x15\x94\x00\x11g\x98\x13\xcexI].\xc3F\xdaM\xfeB\x9ay\x11\xc7\x81lG:\xc8\xd8y\x8a'



# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/") 
@app.route("/home/", methods = ["GET","POST"])

def welcome():
	if "user" in session:
		return render_template("loggedin.html", usr = session["user"])
	else:
		if "statusUpdate" in request.args:
			return render_template('login.html', footer = request.args["statusUpdate"])
		else:
			return render_template('login.html', footer = "You have not logged in yet!")


	
# Register page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/register/", methods = ["POST"]) 

def signUp():
	d = request.form 
	if d["password1"] == d["password2"] and len(d["username"]) > 0 and len(d["password1"]) > 0:
		accountFile = open("data/accounts.csv" , "a")
		if accExist(d["username"]):
			return redirect(url_for('welcome', statusUpdate = "This username already exists! Please choose a new one."))
		accountFile.write(d["username"] + "," + hashlib.sha512(d["password1"]).hexdigest() + "\n")   
		accountFile.close()       
		return redirect(url_for("welcome", statusUpdate = "You have created a new account!"))
	else:
		return redirect(url_for('welcome', statusUpdate = "Your credentials are invalid. Please  double check that you have filled out the username/password slots and that your passwords match!"))
	
   

 # Login page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/login/", methods = ["POST"]) 

def login():
    d = request.form 
    # ~~~~~~~~~~~~~
    reader = csv.reader(open("data/accounts.csv", "r"))
    if not accExist(d["username"]):
        return redirect(url_for('welcome', statusUpdate = "This username does not exist!"))
    else:
    	reader = csv.reader(open("data/accounts.csv", "r"))
    	acc = {}
    	for row in reader:
    		k, v = row
    		acc[k] = v
        if hashlib.sha512(d["password"]).hexdigest() == acc[d["username"]]: 
            session["user"] = d["username"]
            return redirect(url_for('welcome'))
        else:
        	return redirect(url_for('welcome', statusUpdate = "Your password is incorrect"))

# Log out page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/logout/", methods = ['POST'])
def logout():
    session.pop("user")
    return redirect(url_for('welcome'))


def accExist(usr):
	reader = csv.reader(open("data/accounts.csv", "r"))
	acc = {}
	for row in reader:
		k, v = row
		acc[k] = v
		if usr in acc.keys():
			return True
		else:
			return False





if __name__ == '__main__':
    app.debug = True
    app.run()

