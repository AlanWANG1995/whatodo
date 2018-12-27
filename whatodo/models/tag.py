from ..app import db
class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uuid = db.Column(db.String(36))
  label = db.Column(db.Text, nullable=False)

  def __iter__(self):
    return iter({
      "id": self.id,
      "uuid": self.uuid,
      "label": self.label
    }.items())

  def __eq__(self, uuid:str):
    return uuid == self.uuid