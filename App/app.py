from flask import Flask, render_template, request
from game_logic import play_game

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def game():
    message = "Your mission is to find the treasure!"
    step = 1
    choices = {}

    if request.method == 'POST':
        choice1 = request.form.get('choice1')
        choice2 = request.form.get('choice2')
        choice3 = request.form.get('choice3')

        choices['choice1'] = choice1
        choices['choice2'] = choice2
        choices['choice3'] = choice3

        # Determine which step we're on
        if choice1 and not choice2:
            message = play_game(choice1)
            step = 2
        elif choice1 and choice2 and not choice3:
            message = play_game(choice1, choice2)
            step = 3
        elif choice1 and choice2 and choice3:
            message = play_game(choice1, choice2, choice3)
            step = 1  # Reset for new game
            choices = {}

    return render_template('index.html', message=message, step=step, choices=choices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

