from whatodo.models import Todo
class TestTodo:
  def test_todo_save(self,new_todo):
    todo = new_todo()
    todo.save()
    assert Todo.query.filter_by(uuid=todo.uuid).first() is not None
    pass

  def test_todo_contain_and_destroy(self, origin_user):
    uuid = "de820d07-ac84-4ce5-b65f-c5bc433b95b7"
    content = "test todo"
    user_uuid = origin_user.uuid
    todo = Todo.create(uuid=uuid, content=content, user=user_uuid)
    assert Todo.query.filter_by(uuid=uuid).first() is not None
    todo.destroy()
    assert Todo.query.filter_by(uuid=uuid).first() is None

    
    