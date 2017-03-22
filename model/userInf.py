from mongoengine import Document, StringField

class UserINF(Document):
    username = StringField();
    address = StringField();
    phone_number = StringField();
