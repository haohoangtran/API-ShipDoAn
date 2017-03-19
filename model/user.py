from mongoengine import Document, StringField, FloatField, IntField

class User(Document):
    username = StringField();
    password = StringField();
    address = StringField();
    total_spend = FloatField();
    spend = FloatField();