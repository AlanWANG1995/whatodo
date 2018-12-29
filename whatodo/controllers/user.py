from ..app import app, request, jsonify,db
import uuid
from .helper import *
from ..models import User

@api
def create(email):
  if not User.contain(email=email):
    user_uuid = str(uuid.uuid4())
    me: User = User.create(user_uuid, email)
    return jsonify(error_json[201]), 201
  else:
    return jsonify(error_json[409]), 409

@api
def show(email=None, uuid=None):
  if email:
    me = User.find(email=email)
    return model_or_404(me)
  else:
    me = User.find(uuid=uuid)
    return model_or_404(me)

@api
def destroy(email=None, uuid=None):
  if email:
    me = User.find(email=email)
  else:
    me = User.find(uuid=uuid)
  if me:
    me.destroy()
    return jsonify(error_json[200]), 200
  else:
    return jsonify(error_json[404]), 404