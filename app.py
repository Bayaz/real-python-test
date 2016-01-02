#_________________FLASK HELLO WORLD________________________#

#Step 1 import the Flask class from Flask package
from flask import Flask

#Step 2 create the application object or instance
app = Flask(__name__)

#Step 3 use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#Step 4 define a view using a function that returns a string
def hello_world():
    return "Hello, World!"

#Step 5 start development server using the run() method
if __name__ == "__main__":
    app.run()










