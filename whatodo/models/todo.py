from ..app import db
from .user import User

class Todo(db.Model):
  uuid = db.Column(db.String(36), primary_key=True)
  content = db.Column(db.Text, nullable=False)
  emergency_level = db.Column(db.Integer, default=0)
  finish = db.Column(db.Boolean, default=False)
  user_uuid = db.Column(db.String(36), db.ForeignKey('user.uuid'), nullable=False)

  @staticmethod
  def create(**kwarg):
    todo = Todo()
    todo.uuid = kwarg["uuid"]
    todo.content = kwarg["content"]
    todo.emergency_level = 0 if "emergency_level" not in kwarg else kwarg["emergency_level"]
    todo.finish = False if "finish" not in kwarg else kwarg["emergency_level"]
    todo.user_uuid = kwarg["user"]
    return todo

  @staticmethod
  def contain(uuid:str)->bool:
    return Todo.query.filter_by(uuid=uuid).first() is None


  def __json__(self)->dict:
    return {
      "uuid": self.uuid,
      "content": self.content,
      "emergency_level": self.emergency_level,
      "finish": self.finish,
      "user_uuid": self.user_uuid
    }

  def __eq__(self, uuid:str)->bool:
    return uuid == self.uuid