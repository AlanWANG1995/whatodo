from whatodo.app import app, db
import os,tempfile
import pytest

@pytest.fixture(scope="session")
def context():
  db_fd, app.config["DATABASE"] = tempfile.mkstemp()
  app.config["TESTING"] = True
  app.config["SQLALCHEMY_ECHO"] = False
  app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + app.config["DATABASE"]
  with app.app_context() as context:
    db.init_app(app)
    context.push()
    db.create_all()
    yield context
  os.close(db_fd)
  os.unlink(app.config["DATABASE"])


@pytest.fixture
def client():
  pass