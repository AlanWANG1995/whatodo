import uuid
from .helper import *
from ..app import app,request, jsonify,db
from ..models import Todo,User
from ..models.helper import *

@api
def create(user:str, content:str):
  if User.contain(uuid=user):
    todo: Todo = Todo.create(uuid=str(uuid.uuid4()), content=content, user=user)
    db.session.add(todo)
    db.session.commit()
    return jsonify(error_json[201]), 201
  else:
    return jsonify(error_json[400]), 400

@api
def show(uuid:str):
  todo = Todo.query.filter_by(uuid=uuid).first()
  return model_or_404(todo)

@api
def index(user:str, tag:str=None, finish:bool=False):
  todoes = Todo.query.filter_by(user_uuid=user, finish=finish).all()
  return model_or_404(todoes)

@api
def done(uuid:str):
  todo = Todo.query.filter_by(uuid=uuid).update(finish=True)
  return jsonify(error_json[200]), 200
