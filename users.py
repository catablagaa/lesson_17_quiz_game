import json


def add_user(player_id: str, all_players: dict, path: str = "users.json") -> dict:

    full_name = input("Introduceti numele (optional): ")
    full_name = player_id if full_name == "" or not full_name.isalnum() else full_name
    passwd = ""
    confirm_passwd = " "

    while len(passwd) < 3:
        while passwd != confirm_passwd:
            passwd = input("Introdu parola ta: ")
            confirm_passwd = input("Confirma parola: ")
        if len(passwd) < 3:
            passwd = ""
            confirm_passwd = " "
            print("Parola este prea scurta")

    new_user = {player_id: {"full_name": full_name, "high_score": 0, "password": passwd}}
    all_players.update(new_user)

    with open(path, "r+") as f:
        f.write(json.dumps(all_players, indent=4))

    return new_user



def login(path: str = "users.json"):
    new_user = {}
    is_new_user = False
    user = input("Logheaza-te: ")
    with open(path, "r") as f:
        users = json.loads(f.read())

    if user not in users:
        user_pick = input("Doresti sa te inscrii ca nou jucator? Y/N: ")
        if user_pick.lower() == "y":
            new_user = add_user(player_id=user, all_players=users)
            is_new_user = True
        else:
            while user not in users:
                user = input("Logheaza-te, utilizatorul nu exista: ")

    if not is_new_user:
        passwd = input("Introduceti parola: ")
        counter = 0
        while passwd != users[user]["password"]:
            passwd = input("Introduceti parola: ")
            counter += 1
            if counter == 3:
                raise Exception("Parola a fost introdusa gresit de prea multe ori!")
    else:
        return new_user

    return {user: users[user]}
