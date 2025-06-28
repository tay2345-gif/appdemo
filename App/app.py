from flask import Flask, request, jsonify
from game_logic import play_game

app = Flask(__name__)

@app.route('/')
def index():
    return "🕵️ Welcome to 007 Island (DevOps Edition). Use /play endpoint."

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    choice1 = data.get('choice1')
    choice2 = data.get('choice2')
    choice3 = data.get('choice3')

    result = play_game(choice1, choice2, choice3)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
