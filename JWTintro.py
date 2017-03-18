from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from mongoengine import Document,StringField
from db_class import User,Food
from task_resource import TaskListRest, TaskRes, UserListRes
import datetime
import mlab

app = Flask(__name__)
api = Api(app)

app.config["SECRET_KEY"]="SHIP DO AN DEM"

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600)
}

mlab.connect()

food = Food(name = "VIT OM SAU", url = "www.facebook.com",coint_old = "bitcoint", coint_new = "cointnew", cout_rate = 9, rate = 0.85)
food.save()

for food in Food.objects():
    # food.delete()
    print(mlab.itemjson(food))

for user in User.objects():
    print(mlab.itemjson(user))


class LoginCredentials(Resource):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def authenticate(username, password):
        for user in User.objects().filter(username=username):
            if user.password == password:
                return LoginCredentials(str(user.id), user.username, user.password)

    def identity(payload):
        user_id = payload["identity"]
        user = User.objects().with_id(user_id)
        if (user_id is not None):
            return LoginCredentials(str(user.id), user.username, user.password)

    jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


@app.route('/')
# @jwt_required()
def hello_world():
    return 'Hello World!'

api.add_resource(TaskListRest,"/tasks")
api.add_resource(TaskRes,"/tasks/<task_id>")
api.add_resource(UserListRes,"/register")


if __name__=='__main__':
    app.run()