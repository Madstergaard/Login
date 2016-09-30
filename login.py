from flask import Flask, render_template, request # Capital Flask is a subset of the module flask

app = Flask(__name__)


# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/") # decorator, goes directly above funtion header, the 
                # "/" (route) for webpage will run this function
@app.route("/login/")


def welcome():
    print request.headers # contains metadata about request
    return render_template('login.html')



# Authentication page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/authenticate/", methods = ["GET", "POST"]) # routed to after submit bc of 
                             # form action = "/authenticate/"
def auth():                # NOTE: we are using POST requests
	
	user = "cleo"
	pswd = "patra"
	filled_form = request.form
	if filled_form["username"] == user and filled_form["password"] == pswd:
		success = "You have successfully logged in!"
	else :
		success = "You have failed to log in :("
	
	return render_template('authenticate.html', header = success )

if __name__ == '__main__':
    app.debug = True
    app.run()

