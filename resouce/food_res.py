from flask_restful import Resource, reqparse
import mlab
from model.food import Food
from model.user import User
from flask_jwt import JWT, jwt_required

class UserRestList(Resource):
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

        user = User(username=username, password=password, address=address, spend=spend)
        user.save()

        return mlab.itemjson(user)


class FoodRestList(Resource):


    def get(self):
        food = Food.objects()
        return mlab.item2json(food)


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="url", type=str, location="json")
        parser.add_argument(name="coint_old", type=str, location="json")
        parser.add_argument(name="coint_new", type=str, location="json")
        parser.add_argument(name="cout_rate", type=int, location="json")
        parser.add_argument(name="rate", type=float, location="json")
        body = parser.parse_args()
        name = body.name
        url = body.url
        coint_old = body.coint_old
        coint_new = body.coint_new
        cout_rate = body.cout_rate
        rate = body.rate
        food = Food(name=name, url=url, coint_new=coint_new, coint_old=coint_old, cout_rate=cout_rate, rate=rate)
        food.save()
        add_food = Food.objects().with_id(food.id)
        return mlab.item2json(add_food)

class FoodRest(Resource):

    def get(selfk,food_id):
        food = Food.objects().with_id(food_id)
        return mlab.item2json(food)



    def delete(self,food_id):
        food = Food.objects().with_id(food_id)
        food.delete()
        if food != None:
            return {"message":"delete successful"}
        else:
            return {"message":"not found food"}

    def put(self,food_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="url", type=str, location="json")
        parser.add_argument(name="coint_old", type=str, location="json")
        parser.add_argument(name="coint_new", type=str, location="json")
        parser.add_argument(name="cout_rate", type=int, location="json")
        parser.add_argument(name="rate", type=float, location="json")
        body = parser.parse_args()
        name = body.name
        url = body.url
        coint_old = body.coint_old
        coint_new = body.coint_new
        cout_rate = body.cout_rate
        rate = body.rate
        food = Food.objects().with_id(food_id)
        food.update(name=name, url=url, coint_new=coint_new, coint_old=coint_old, cout_rate=cout_rate, rate=rate)

        add_food = Food.objects().with_id(food.food_id)
        return mlab.item2json(add_food)