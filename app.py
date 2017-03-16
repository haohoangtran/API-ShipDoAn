from flask import Flask
import mlab
from flask_restful import Api
from resouce.food_res import FoodRes

mlab.connect()

app = Flask(__name__)

api = Api(app)
api.add_resource(FoodRes,"/food")
@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

if __name__ == '__main__':
    app.run()
