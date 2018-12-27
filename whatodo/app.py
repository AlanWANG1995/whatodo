from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app:Flask = Flask(__name__)
app.config.from_pyfile('settings.cfg')
db:SQLAlchemy = SQLAlchemy(app)


from .models import User
from .models import Tag
from .models import Todo

db.drop_all()
db.create_all()

import uuid

@app.route("/user", methods=["POST"])
def create_user():
  content = request.json
  if "email" in content:
    if not User.contain(email=content["email"]):
      me: User = User.create(str(uuid.uuid4()), content["email"])
      db.session.add(me)
      db.session.commit()
      return jsonify(dict(me))
    else:
      return jsonify(dict(User.query.filter_by(email=content["email"]).first()))
  else:
    return jsonify({"status": "400", "message": "invalid parameters"}), 400

@app.route("/todo", methods=["POST"])
def create_todo():
  content = request.json
  if User.contain(uuid=content["user"]):
    todo: Todo = Todo.create(uuid=str(uuid.uuid4()), content=content["content"], user=content["user"])
    db.session.add(todo)
    db.session.commit()
    return jsonify(dict(todo))
  else:
    return jsonify({"status": "400", "message": "invalid parameters"}), 400
  
