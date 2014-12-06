from flask import Flask, render_template, Response
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

mongo = MongoClient()

db = mongo.undp

# / = Homepage
@app.route('/')
def hello_world():
    fjalori = {"good":"mire","bad":"keq"}

    return render_template("index.html", fjalori=fjalori)

@app.route('/json/<string:gender>')
def json(gender):
    result = db.gsc.find({"surveyee.gender": gender})
    print result

    return Response(response=json_util.dumps(result), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)
