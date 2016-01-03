#_________________FLASK HELLO WORLD________________________#

#Step 1 import the Flask class from Flask package
from flask import Flask

#Step 2 create the application object or instance
app = Flask(__name__)

#error handling ...dont have to restart server to see changes now..just refresh browser
app.config["DEBUG"] = True

#Step 3 use decorators to link the function to a url making static routes, functions for static routes must come before dynamic routes
@app.route("/")
@app.route("/hello")

#Step 4 define a view using a function that returns a string !
def hello_world():
    return "Hello, World!?!?!?!?!?"

#@app.route("/test") #notice how this doesn't work with dynamic test<search query> below
#add a dynamic route...note that it will not work for just test
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#you can specify what routes return..like this
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

#200 is not required....flask automatically does this for us
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello {}".format(name), 200
	else:
		return "Not Found at All!!", 404	

#Step 5 start development server using the run() method
if __name__ == "__main__":
    app.run()










