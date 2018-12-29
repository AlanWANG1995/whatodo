from whatodo.models import User, Todo
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
    assert not User.contain(uuid=uuid)

  def test_user_add_todo_and_destroy(self):
    todo_uuid0 = "ff9c3807-4a34-4137-83ea-a403efe1343c"
    user_uuid = "4f7e2148-7c44-4dc0-922f-2a7c31c9eda3"
    user = User.create(uuid=user_uuid, email="my_test_user@test.com")
    todo = user.add_todo(uuid=todo_uuid0, content="nothing")
    assert todo.uuid == todo_uuid0
    assert todo.user_uuid == user_uuid
    assert Todo.contain(uuid=todo_uuid0)
    user.destroy()
    assert not Todo.contain(uuid=todo_uuid0)