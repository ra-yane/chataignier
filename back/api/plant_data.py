from flask_restful import Resource
from flask import request
import json
import datetime

from models import Plant


def insert_plant_data(temperature, humidity):
    Plant.insert(temperature=temperature, humidity=humidity).execute()


def get_last_hour_plant_data():
    output = {
        'temperature': [],
        'humidity': [],
        'date': []
    }
    last_hour = Plant.select()\
        .order_by(Plant.date.asc())\
        .limit(6)
    for measure in last_hour:
        output['temperature'].append(float(measure.temperature))
        output['humidity'].append(float(measure.humidity))
        output['date'].append({
                'hour': datetime.datetime.fromtimestamp(measure.date / 1e3).hour - 1,
                'minute': datetime.datetime.fromtimestamp(measure.date / 1e3).minute
            })
    return output


class PlantData(Resource):

    def get(self):
        return {'msg': 'success', 'stats': get_last_hour_plant_data()}

    def post(self):
        """

        POST request used by the agent to post the plant data into the Database.
        :return: Success if plant data is successfully sent, Error 400 otherwise
        """
        body = request.data
        batch = json.loads(body)
        if batch:
            insert_plant_data(batch['temperature'],batch['humidity'])
            return {"msg": "success"}
        else:
            return {"error": "No data has been sent. Please check the card."}, 400

