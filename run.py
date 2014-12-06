from flask import Flask, render_template, Response
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

# Krijojme instance te klases MongoClient
mongo = MongoClient()

# Krijojme instance te databazes qe do ta perdorim ne MongoDB
db = mongo.undp

# Homepage
@app.route('/')
def hello_world():
    fjalori = {"good":"mire","bad":"keq"}

    return render_template("index.html", fjalori=fjalori)

# http://localhost:5000:/json/<string:gender>
@app.route('/json/<string:gender>')
def json(gender):

    # Bejme find() ne MongoDB duke i kaluar variablen gender te marrur nga URL si parameter
    result = db.gsc.find({"surveyee.gender": gender})

    print result

    # Kthejme pergjigjen duke i caktuar tipin e mimetype application/json
    # E konvertojme objektin(coursor) qe na eshte kthyer nga MongoDB para se ta kalojme ne reponse me json_util.dumps()
    return Response(response=json_util.dumps(result), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)
