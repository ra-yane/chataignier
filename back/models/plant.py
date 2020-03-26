from peewee import *
import datetime

plant_db = SqliteDatabase('db/plant.db')


class Plant(Model):
    id = AutoField(primary_key=True)
    temperature = CharField()
    humidity = CharField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = plant_db


with plant_db:
    Plant.create_table(fail_silently=True)
