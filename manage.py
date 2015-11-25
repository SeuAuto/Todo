from app import app
from app.models import Todo
from flask.ext.script import Manager

manager = Manager(app)

@manager.command
def save():
    todo = Todo(content="jj")
    todo.save()

@manager.command
def query_all():
    todos = Todo.objects.all()
    for one in todos:
        print one["content"]



if __name__ == '__main__':
    manager.run()