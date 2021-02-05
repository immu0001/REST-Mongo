from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Imran:IMimran123@task-pro-cluster.ucykv.mongodb.net/La_Tarea?retryWrites=true&w=majority')

db = client.La_Tarea
col = db.Tarea_Col
cursor = col.find({})


app = Flask(__name__)
api = Api(app)

class LastOne(Resource):
    def get(self):
        return str(col.find_one())


class AllDocs(Resource):

    def get(self):
        all = ""
        for document in col.find({}):
            all = all + str(document)
        return all


api.add_resource(AllDocs, "/")
api.add_resource(LastOne, "/LastOne")
#api.add_resource(AllDocs, "/AllDocs")

if __name__ == '__main__':
    app.run(debug=True)

