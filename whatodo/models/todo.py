from ..app import db
from .user import User

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uuid = db.Column(db.String(36))
  content = db.Column(db.Text, nullable=False)
  emergency_level = db.Column(db.Integer, default=0)
  finish = db.Column(db.Boolean, default=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  @staticmethod
  def create(**kwarg):
    todo = Todo()
    todo.uuid = kwarg["uuid"]
    todo.content = kwarg["content"]
    todo.emergency_level = 0 if "emergency_level" not in kwarg else kwarg["emergency_level"]
    todo.finish = False if "finish" not in kwarg else kwarg["emergency_level"]
    todo.user_id = User.query.filter_by(uuid=kwarg["user"]).first().id
    return todo


  def __iter__(self):
    return iter({
      "id": self.id,
      "uuid": self.uuid,
      "content": self.content,
      "emergency_level": self.emergency_level,
      "finish": self.finish,
      "user_id": self.user_id
    }.items())

  def __eq__(self, uuid:str):
    return uuid == self.uuid