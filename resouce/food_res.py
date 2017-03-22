from flask_restful import Resource, reqparse
import mlab
from model.food import Food
from model.user import User
from model.order import Order
from model.userInf import UserINF
from flask_jwt import JWT, jwt_required

class UserRestList(Resource):

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(name="username", type=str, location="json")
        parser.add_argument(name="password", type=str, location="json")
        parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="spend", type=float, location="json")
        parser.add_argument(name="total_spend", type=float, location="json")

        body = parser.parse_args()

        username = body["username"]
        password = body["password"]
        address = body["address"]
        spend = body["spend"]
        total_spend = body["total_spend"]

        user = User(username=username, password=password, address=address, spend=spend, total_spend = total_spend)
        user.save()

        return mlab.item2json(user)


    def get(self):
        user = User.objects();
        return mlab.item2json(user)

class UserRestFacebookList(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(name="username", type=str, location="json")
        parser.add_argument(name="password", type=str, location="json")
        parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="spend", type=float, location="json")
        parser.add_argument(name="total_spend", type=float, location="json")

        body = parser.parse_args()

        username = body["username"]
        password = body["password"]
        address = body["address"]
        spend = body["spend"]
        total_spend = body["total_spend"]


        user = User(username=username, password=password, address=address, spend=spend, total_spend=total_spend)
        user.save()

        return mlab.item2json(user)


class UserRest(Resource):
    def get(self,user_id):
        user = User.objects();
        return mlab.item2json(user);

    def put(self,user_id):
        parser = reqparse.RequestParser();
        parser.add_argument(name="username", type=str, location="json")
        # parser.add_argument(name="password", type=str, location="json")
        # parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="spend", type=float, location="json")

        body = parser.parse_args()

        username = body["username"]
        # password = body["password"]
        # address = body["address"]
        spend = body["spend"]

        user = User.objects().with_id(user_id)
        total_spend_last = user.total_spend;

        user.update(username=username, total_spend=spend+total_spend_last);

        user_update = User.objects().with_id(user_id)
        return mlab.item2json(user_update)


class UserINFRest(Resource):
    def get(self):
        user = UserINF.objects().with_id(userInfo_id);
        return mlab.item2json(user);

    def post(self):
        parser = reqparse.RequestParser();
        parser.add_argument(name="username", type=str, location="json")
        parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="phone_number", type=str, location="json")

        body = parser.parse_args()

        username = body["username"]
        address = body["address"]
        phone_number = body["phone_number"]

        user = UserINF(username=username, address=address, phone_number=phone_number)
        user.save()

        # add_user = UserINF.objects.with_id(userInfo_id)

        # user = UserINF.objects().with_id(userInfo_id)
        # user.update(username=username, address=address, phone_number=phone_number);

        return mlab.item2json(user)



class FoodRestList(Resource):


    def get(self):
        food = Food.objects()
        return mlab.list2json(food)


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

class FoodRestInfo(Resource):

    def get(selfk,food_id):
        food = Food.objects().with_id(food_id)
        return mlab.item2json(food)


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
        parser.add_argument(name="rate", type=float, location="json")
        body = parser.parse_args()
        # name = body.name
        # url = body.url
        # coint_old = body.coint_old
        # coint_new = body.coint_new
        # cout_rate = body.cout_rate
        rate_res = body.rate
        food = Food.objects().with_id(food_id)
        cout_rate=food.cout_rate
        rate=food.rate
        rate_new=(cout_rate*rate +rate_res)/(cout_rate+1)
        food.update( cout_rate=cout_rate+1, rate=rate_new)
        add_food = Food.objects().with_id(food_id)
        return mlab.item2json(add_food)

class OrderRestList(Resource):
    def get(self):
        order_list = Order.objects()
        return mlab.list2json(order_list)

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(name = "username", type = str, location = "json")
        parser.add_argument(name = "userid", type = str, location = "json")
        parser.add_argument(name = "food_name", type = str, location = "json")
        parser.add_argument(name = "orderdate", type = str, location = "json")
        parser.add_argument(name = "rate", type = float, location = "json")
        parser.add_argument(name = "food_number", type = int, location = "json")

        body = parser.parse_args()

        username = body.username
        userid = body.userid
        food_name = body.food_name
        orderdate = body.orderdate
        rate = body.rate
        food_number = body.food_number

        order = Order(username = username, userid = userid, food_name = food_name, orderdate = orderdate, rate = rate, food_number = food_number)
        order.save()

        return mlab.item2json(order)

class OrderRest(Resource):
    def get(self,order_id):
        order = Order.objects().with_id(order_id)
        return mlab.item2json(order)


    def put(self,order_id):
        parser = reqparse.RequestParser()

        parser.add_argument(name = "username", type = str, location = "json")
        parser.add_argument(name = "userid", type = str, location = "json")
        parser.add_argument(name = "food_name", type = str, location = "json")
        parser.add_argument(name = "orderdate", type = str, location = "json")
        parser.add_argument(name = "rate", type = float, location = "json")
        parser.add_argument(name = "food_number", type = int, location = "json")

        body = parser.parse_args()

        username = body.username
        userid = body.userid
        food_name = body.food_name
        orderdate = body.orderdate
        rate = body.rate
        food_number = body.food_number

        order = Order.objects().with_id(order_id)
        order.update(username = username, userid = userid, food_name = food_name, orderdate = orderdate, rate = rate, food_number = food_number)

        return mlab.item2json(order)



