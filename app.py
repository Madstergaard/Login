from flask import Flask, render_template, request # Capital Flask is a subset of the module flask

app = Flask(__name__)



# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/") # decorator, goes directly above funtion header, the 
                # "/" (route) for webpage will run this function
@app.route("/login/")

def welcome():
    print request.headers # contains metadata about request


    return render_template('button.html')

@app.route("/authenticate/", methods = ["GET", "POST"]) # routed to after submit bc of 
                             # form action = "/authenticate/"

def auth():                # NOTE: we are using get requests
	print request.form
	print request.form['user']
	return "OK"

if __name__ == '__main__':
    app.debug = True
    app.run()

