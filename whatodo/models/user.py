from ..app import db
from .todo import Todo
from .helper import *
class User(db.Model):
  uuid = db.Column(db.String(36), nullable=False, primary_key=True)
  email = db.Column(db.String(50), nullable=False)
  todoes = db.relationship('Todo', backref='user', lazy='select')

  def __json__(self)->dict:
    return {
      "uuid": self.uuid
    }

  @staticmethod
  def create(uuid:str, email:str):
    user = User()
    user.uuid = uuid
    user.email = email
    db.session.add(user)
    db.session.commit()
    return user
  
  @staticmethod
  def find(**kargs):
    return User.query.filter_by(**kargs).first()

  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def clear_todoes(self):
    for todo in self.todoes:
      todo.destroy()

  def add_todo(self, *args, **kargs):
    kargs["user"] = self.uuid
    return Todo.create(*args, **kargs)

  @before(clear_todoes)
  def destroy(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def contain(**kwarg) -> bool:
    return User.query.filter_by(**kwarg).first() is not None

  def __eq__(self, uuid:str):
    return uuid == self.uuid