def play_game(choice1, choice2=None, choice3=None):
    choice1 = choice1.lower()

    if choice1 != "left":
        return "💥 IT WAS A TRAP! TRY AGAIN, AGENT!"

    if choice2 is None:
        return "You've come to a lake. Wait for a boat or swim across? (wait/swim)"

    choice2 = choice2.lower()
    if choice2 != "wait":
        return "🌊 YOU WERE CAPTURED BY ENEMY DIVERS! GAME OVER."

    if choice3 is None:
        return "You arrive at the island. Choose a door: red, yellow, blue."

    choice3 = choice3.lower()
    if choice3 == "yellow":
        return "🎉 YOU FOUND THE TREASURE, AGENT! MISSION ACCOMPLISHED!"
    elif choice3 == "red":
        return "🔥 It's a trap! The room bursts into flames. GAME OVER."
    elif choice3 == "blue":
        return "🐊 You enter a room full of alligators. GAME OVER."
    else:
        return "🚪 That door doesn't exist. GAME OVER."
