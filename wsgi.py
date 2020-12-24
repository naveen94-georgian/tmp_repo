from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb+srv://dprog123:dprog@weather-cluster.t8pf8.mongodb.net")
db_name='weather-db'
doc_name='weather-collection'
db = client[db_name]
collection = db[doc_name]

class Weather(Resource):
    def get(self):
        filter={}
        city = request.args.getlist('city')
        if len(city) > 0:
            filter['City'] = city[0]
        day = request.args.getlist('day')
        if len(day) > 0:
            filter['Day'] = day[0]
        month = request.args.getlist('month')
        if len(month) > 0:
            filter['Month'] = month[0]
        year = request.args.getlist('year')
        if len(year) > 0:
            filter['Year'] = year[0]
        
        documents = collection.find(filter)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

api.add_resource(Weather, '/weather')
@app.route('/')
def index():
    return '<p>Index Page</p>'



if __name__ == '__main__':
    app.debug = True
    app.run()