import random
import json


def create_map():
    # Load map name json file and store in dictionary
    location_file = "game_data/location_names.json"
    with open(location_file) as location_names_json:
        location_names = json.load(location_names_json)

    # Shuffle map list expect first and last items
    for level, maps in location_names.items():
        middle_map = maps[1:-1]
        random.shuffle(middle_map)
        location_names[level] = [maps[0]] + middle_map + [maps[-1]]

    # Initialize maps
    maps = {"level_1_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_2_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_3_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_4_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_5_map": {(x, y): "" for x in range(5) for y in range(4)}}

    # Assign location name to maps
    for level, locations in zip(maps.keys(), location_names.values()):
        for index, each_map in enumerate(maps[level]):
            maps[level][each_map] = locations[index]

    return maps


def create_character(character_information):
    character = {"name": character_information.name, "occupation": character_information.occupation_title,
                 "location": (0, 0), "level": 0, "current_hp": 10, "max_hp": 10, "xp": 100,
                 "attack": character_information.skills}
    return character


def get_user_input_for_character():
    # Get username from user
    print("Welcome User! Enter your name to start")
    character_information = {}
    while True:
        try:
            name = input("Your name: ")
            if len(name.strip()) <= 2:
                pass
                # TODO: raise appropriate error
                # raise
        except:
            print("Character name should be longer than 2 letters.😥")
            print("Please re-enter your name🙏")
        else:
            character_information["name"] = name
            break

    # Get user occupation
    occupation_list = ["Otaku", "Salaryman", "Ninja", "Samurai"]


def check_for_foe():
    #  25% of chance to encounter a foe
    there_is_a_foe = random.randint(1, 4)
    if there_is_a_foe == 1:
        return True
    else:
        return False

def fight_with_foe():
    # Load foe name json file and store in dictionary
    foe_file = "game_data/foe.json"
    with open(foe_file) as foe_json:
        foes = json.load(foe_json)

    chosen_foe = random.choice(foes)
    pass


def main():
    print("I'm ready for the term project! 🙌")
    game_map = create_map()
    get_user_input_for_character()
    there_is_a_challenger = check_for_foe()
    if there_is_a_challenger:
        fight_with_foe()





if __name__ == "__main__":
    main()
