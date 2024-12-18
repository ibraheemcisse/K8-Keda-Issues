from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Rock-Paper-Scissors!"

@app.route("/play/<user_choice>")
def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    return {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    }

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
