from mongoengine import *

class Food(Document):
    name=StringField()
    url=StringField()
    coint_old=StringField()
    coint_new=StringField()
    cout_rate=IntField()
    rate=FloatField()
    # nếu đánh giá thêm 1 lần = rate*cout_rate +đánh giá chia (count_rate+1)