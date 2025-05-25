from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from queenDAO import queenDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
@cross_origin()
def index():
    return "Hello, Hello, Hello!"

#curl "https://niallrussell93.pythonanywhere.com/queen"
@app.route('/queen')
@cross_origin()
def getAll():
    #print("in getall")
    results = queenDAO.getAll()
    return jsonify(results)

#curl "https://niallrussell93.pythonanywhere.com/queen/2"
@app.route('/queen/<int:id>')
@cross_origin()
def findById(id):
    foundQueen = queenDAO.findByID(id)

    return jsonify(foundQueen)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Latrice Royale\", \"age_on_show\":39, \"season\":4, \"place\":4,\"city\":\"South Beach\"}" https://niallrussell93.pythonanywhere.com/queen

@app.route('/queen', methods=['POST'])
@cross_origin()
def create():

    if not request.json:
        abort(400)
    # other checking
    queen = {
        "name": request.json['name'],
        "age_on_show": request.json['age_on_show'],
        "season": request.json['season'],
        "place": request.json['place'],
        "city": request.json['city']
    }
    addedqueen = queenDAO.create(queen)

    return jsonify(addedqueen)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Alaska\", \"age_on_show\":27, \"season\":5, \"place\":2,\"city\":\"Pittsburgh\"}" http://127.0.0.1:5000/queen/18
@app.route('/queen/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundQueen = queenDAO.findByID(id)
    if not foundQueen:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'age_on_show' in reqJson and type(reqJson['age_on_show']) is not int:
        abort(400)
    if 'season' in reqJson and type(reqJson['season']) is not int:
        abort(400)
    if 'place' in reqJson and type(reqJson['place']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundQueen['name'] = reqJson['name']
    if 'age_on_show' in reqJson:
        foundQueen['age_on_show'] = reqJson['age_on_show']
    if 'season' in reqJson:
        foundQueen['season'] = reqJson['season']
    if 'place' in reqJson:
        foundQueen['place'] = reqJson['place']
    if 'city' in reqJson:
        foundQueen['city'] = reqJson['city']
    queenDAO.update(id,foundQueen)
    return jsonify(foundQueen)

@app.route('/queen/<int:id>' , methods=['DELETE'])
@cross_origin()
def delete(id):
    queenDAO.delete(id)
    return jsonify({"done":True})


@app.route('/franchise')
@cross_origin()
def getAllFranchises():
    results = queenDAO.getAllFranchises()
    return jsonify(results)

@app.route('/franchise', methods=['POST'])
@cross_origin()
def createFranchise():
    if not request.json or 'name' not in request.json:
        abort(400)
    franchise = {
        "name": request.json['name']
    }
    addedfranchise = queenDAO.createFranchise(franchise)
    return jsonify(addedfranchise)



if __name__ == '__main__' :
    app.run(debug= True)