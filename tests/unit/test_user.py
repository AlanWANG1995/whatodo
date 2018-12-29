from whatodo.models import User
from whatodo.app import db
import pytest

class TestUser:
  def test_save_user(self,new_user):
    user = new_user()
    user.save()
    assert User.query.filter_by(uuid=user.uuid).first() is not None
    return
  
  def test_contain_user(self):
    uuid = "9050ce38-3cf2-4453-9ea2-625e9cbbba08" 
    assert User.contain(uuid=uuid)