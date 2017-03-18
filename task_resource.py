from flask_restful import Resource,reqparse
from db_class import Food, User
from flask_jwt import JWT,jwt_required
import mlab


class UserListRes(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(name="username", type=str, location="json")
        parser.add_argument(name="password", type=str, location="json")
        parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="spend", type=float, location="json")


        body = parser.parse_args()

        username = body["username"]
        password = body["password"]
        address = body["address"]
        spend = body["spend"]

        user = User(username=username, password=password,address = address, spend = spend)
        user.save()

        return mlab.itemjson(user)

class TaskListRest(Resource):
    @jwt_required()
    def get(self):
        food_list = Food.objects()
        return mlab.listjson(food_list)

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="url", type=float, location="json")
        parser.add_argument(name ="coint_old", type = str, location = "json")
        parser.add_argument(name = "coint_new", type = str, location = "json")
        parser.add_argument(name = "cout_rate", type = int, location = "json")
        parser.add_argument(name = "rate", type = float, location = "json")

        body = parser.parse_args()

        name = body["name"]
        url = body["url"]
        coint_old = body["coint_old"]
        coint_new = body["coint_new"]
        cout_rate = body["cout_rate"]
        rate = body["rate"]

        food = Food(name=name, url=url, coint_old = coint_old, coint_new = coint_new, cout_rate = cout_rate, rate = rate)
        food.save()

        return mlab.itemjson(food)

class TaskRes(Resource):
    @jwt_required()
    def get(self,task_id):
        food = Food.objects().with_id(task_id)
        return mlab.itemjson(food)
    @jwt_required()
    def delete(self,task_id):
        food = Food.objects().with_id(task_id)
        food.delete()
        if food != None:
            return {"meassage":"delete success"}
        else:
            return {"meassage":"food not found"}
    @jwt_required()
    def put(self,task_id):
        parser = reqparse.RequestParser()

        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="url", type=float, location="json")
        parser.add_argument(name="coint_old", type=str, location="json")
        parser.add_argument(name="coint_new", type=str, location="json")
        parser.add_argument(name="cout_rate", type=int, location="json")
        parser.add_argument(name="rate", type=float, location="json")

        body = parser.parse_args()

        name = body["name"]
        url = body["url"]
        coint_old = body["coint_old"]
        coint_new = body["coint_new"]
        cout_rate = body["cout_rate"]
        rate = body["rate"]

        food = Food.objects().with_id(task_id)
        food.update(name=name, url=url, coint_old = coint_old, coint_new = coint_new, cout_rate = cout_rate, rate = rate)
        update_food = Food.objects().with_id(task_id)
        return mlab.itemjson(update_food)



