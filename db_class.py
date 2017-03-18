from mongoengine import Document, StringField, FloatField, IntField

class User(Document):
    username = StringField();
    password = StringField();
    address = StringField();
    spend = FloatField();

class Food(Document):
    name = StringField()
    url = StringField()
    coint_old = StringField()
    coint_new = StringField()
    cout_rate = IntField()
    rate = FloatField()