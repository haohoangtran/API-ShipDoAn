from mongoengine import *
from model.user import User
class Order(Document):
    username = StringField();
    userid = StringField();
    food_name = StringField();
    orderdate = StringField();
    rate = FloatField();
    food_number = IntField();
