from app import db
import datetime

class Todo(db.Document):
    """docstring for Todo"""
    content = db.StringField()
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.IntField(default = 0)
