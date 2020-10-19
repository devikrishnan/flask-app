from flask import Flask           # import flask
from service import ToDoServicoe
from models import Schema
app = Flask(__name__)             # create an app instance

#DNU
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


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


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))

@app.route("/todo/<item_id>", methods["PUT"])
def update_todo():
    return jsonify(ToDoService().update(item_id,request.get_json()))

@app.route("/todo/<item_id>", methods["DELETE"])
def delete_todo():
    return jsonify(ToDoService().delete(item_id))

