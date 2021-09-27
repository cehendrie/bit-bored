#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, abort, request
from flask_mongoengine import MongoEngine

# https://stackabuse.com/guide-to-flask-mongoengine-in-python/

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'bit_board',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

class Bit(db.Document):
    scenario = db.StringField()
    bit = db.StringField()
    author_id = db.StringField()
    bit_date = db.DateTimeField()
    create_date = db.DateTimeField()
    update_date = db.DateTimeField()

# bit_boards = [
#     {'id': 1, 'title': 'Bit 1', 'bit': 'This is the first bit.'},
#     {'id': 2, 'title': 'Bit 2', 'bit': 'This is the second bit.'}
# ]


@app.route('/bits')
def get_bits():
    # return jsonify({'bits_boards': bit_boards})
    bits = Bit.objects()
    return jsonify(bits), 200


@app.route('/bits/<id>')
def get_bit(id: str):
    # bit = [bit for bit in bit_boards if bit['id'] == id]
    # if len(bit) == 0:
    #     abort(404)
    # return jsonify({'bit_board': bit[0]})
    bit = Bit.objects.get_or_404(id=id)
    return jsonify(bit), 200


@app.route('/bits/', methods=['POST'])
def create_bit():
    # if not request.json or not 'bit' in request.json:
    #     abort(400)
    # bit = {
    #     'id': bit_boards[-1]['id'] + 1,
    #     'title': request.json['title'],
    #     'bit': request.json.get('bit', "")
    # }
    # bit_boards.append(bit)
    # return jsonify({'bit_board': bit}), 201
    body = request.get_json()
    bit = Bit(**body).save()
    return jsonify(bit), 201


@app.route('/bits/<id>/', methods=['PUT'])
def update_bit(id):
    body = request.get_json()
    bit = Bit.objects.get_or_404(id=id)
    bit.update(**body)
    return jsonify(str(bit.id)), 200


@app.route('/bits/<id>/', methods=['DELETE'])
def delete_bit(id):
    bit = Bit.objects.get_or_404(id=id)
    bit.delete()
    return jsonify(str(bit.id)), 200


if __name__ == "__main__":
    app.run(debug=True)
