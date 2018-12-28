from ..app import db
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
    return user

  @staticmethod
  def contain(**kwarg) -> bool:
    return User.query.filter_by(**kwarg).first() is not None

  def __eq__(self, uuid:str):
    return uuid == self.uuid