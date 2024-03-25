# Create a quiz game with admin and players. Player has to log in
# if player, then he can play, if admin, he can add questions

import users
import game

if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game!"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    current_player = users.login()

    while True:
        print(f"Let's play {list(current_player.keys())[0]}")
        game.run_game(current_player)
