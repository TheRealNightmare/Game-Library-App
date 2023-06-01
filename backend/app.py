
from flask import Flask, jsonify, request 
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

GAMES = [

    {   'id': uuid.uuid4().hex,
        'title':'Fifa-23',
        'genre':'sports',
        'progress':'10%',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title':'God of war',
        'genre':'Action',
        'progress':'10%',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title':'The last of us',
        'genre':'survival',
        'progress':'10%',
        'played': True,
    },
    {  'id': uuid.uuid4().hex,
        'title':'The forest',
        'genre':'horror/survival',
        'progress':'10%',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title':'mario',
        'genre':'retro',
        'progress':'10%',
        'played': True,
    }

]

@app.route('/', methods=['GET', 'POST'])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'progress': post_data.get('progress'),
            'played': post_data.get('played')})
        response_object['message'] =  'Game Added!'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)


@app.route('/<game_id>', methods =['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'progress': post_data.get('progress'),
            'played': post_data.get('played')
        })
        response_object['message'] =  'Game Updated!'
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Game removed!'    
    return jsonify(response_object)


def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)

