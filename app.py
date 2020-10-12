from flask import Flask           # import flask
from service import ToDoServicoe
from models import Schema
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)           # run the flask app



@app.route("/<name>")
def hello_name(name):
    return "Hello " + name

@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())
