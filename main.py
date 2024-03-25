# Create a quiz game with admin and players. Player has to log in
# if player, then he can play, if admin, he can add questions

import users

if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game!"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    users.login()
