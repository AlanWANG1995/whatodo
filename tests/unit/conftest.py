from whatodo.models import User, Todo
import uuid
import pytest
@pytest.fixture(scope="session")
def origin_user(context):
  return User.create(uuid=str(uuid.uuid4()), email="origin_user@test.com")
@pytest.fixture
def new_user(context):
  id = 0
  def _gen_new_user():
    user = User()
    user.uuid = str(uuid.uuid4())
    user.email = "test_user%s@test.com" % id
    return user
  yield _gen_new_user
  id += 1


@pytest.fixture
def new_todo(context, origin_user):
  id = 0
  def _gen_new_todo():
    todo = Todo()
    todo.uuid = str(uuid.uuid4())
    todo.content = "test todo %s" % id
    todo.user_uuid = origin_user.uuid
    return todo
  yield _gen_new_todo
  id += 1