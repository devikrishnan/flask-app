from flask import Flask           # import flask
from service import ToDoService
from models import Schema
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)           # run the flask app
