"""
Add Docstring
"""
import json
from random import choice, randint

def create_foe():
    """
    Create foes' dictionary from JSON file containing foes information

    :postcondition: get foes information from JSON file and create dictionary from the given information
    :return: a dictionary containing foe information
    """
    foe_file = "game_data/foe.json"
    with open(foe_file, encoding="utf-8") as foe_json:
        foes = json.load(foe_json)
    return foes


def select_foe(foes, level):
    """
    Select one random foe that has the same level with the character

    :param foes: a dictionary
    :param level: an integer representing current character level
    :precondition: foes should be a dictionary containing foes' level as keys and list of foes information as values
    :postcondition: randomly choose a foe that has the same level with the character
    :return: a dictionary containing a foe's information
    """
    return choice(foes[level])


def fight_with_foe(character, foe):
    print(f"A wild {foe['name']} appears!")
    print("")

    while True:
        character["current_hp"] -= foe["attack"]
        print("")
        print(f"|FIGHT🔥| Foe attacked you. Now your hp is {character['current_hp']}")
        print("")

        if character["current_hp"] <= 0:
            return False
        foe["HP"] -= character["attack"]
        print(f"|FIGHT🔥| You attacked foe. Now foe's hp is {foe['HP']}")
        print("")
        if foe["HP"] <= 0:
            print("You WIN!!")
            return True

def check_for_foe():
    #  25% of chance to encounter a foe
    there_is_a_foe = randint(1, 4)
    if there_is_a_foe == 1:
        return True
    else:
        return False

def main():
    pass


if __name__ == "__main__":
    main()