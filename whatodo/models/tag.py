from ..app import db
class Tag(db.Model):
  uuid = db.Column(db.String(36), primary_key=True)
  label = db.Column(db.Text, nullable=False)

  def __json__(self)->dict:
    return {
      "uuid": self.uuid,
      "label": self.label
    }

  def __eq__(self, uuid:str)->bool:
    return uuid == self.uuid