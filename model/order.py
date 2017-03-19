from mongoengine import *
from model.user import User
class Order(Document):
    username = StringField();
    userid = StringField();
    food_name = StringField();
    orderdate = DateTimeField();
    rate = FloatField();
