import flask
from flask_cors import CORS
import functions
import asyncio

app = flask.Flask(__name__)
CORS(app)

@app.route('/madlib', methods=['GET'])
def create():
    return flask.jsonify(asyncio.run(functions.madlibs.main())), 200



app.run(host="0.0.0.0")