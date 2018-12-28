from ..app import app, request, jsonify,db
import uuid
from .helper import *
from ..models import User
from ..models.helper import  *

@api
def create(email):
  if not User.contain(email=email):
    user_uuid = str(uuid.uuid4())
    me: User = User.create(user_uuid, email)
    db.session.add(me)
    db.session.commit()
    return jsonify(error_json[201]), 201
  else:
    return jsonify(error_json[409]), 409

@api
def show(email=None, uuid=None):
  if email:
    me = User.query.filter_by(email=email).first()
    return model_or_404(me)
  else:
    me = User.query.filter_by(uuid=uuid).first()
    return model_or_404(me)
