from flask_restful import Resource, reqparse
import mlab
from model.food import Food


class FoodRes(Resource):
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
        add_food=Food.objects().with_id(food.id)
        return mlab.item2json(food)