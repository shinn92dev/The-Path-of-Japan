"""
Module for handling user movement including validation and actual movement
"""


def validate_movement(user_input, character, board):
    """
    Check if the character's movement based on user input is valid within the board boundaries.

    :param user_input: a string
    :param character: a dictionary containing the character's information
    :param board: a dictionary representing the board
    :precondition: user_input is a string representing the direction of movement, either a cardinal direction or
                   a corresponding number '1' for north, '2' for east, '3' for south, '4' for west
    :precondition: character is a dictionary containing the character's current location with the key 'location'
    :precondition: board must have keys that represent valid location coordinates as tuples (x, y)
    :postcondition: determine if the user's input is valid or not
    :return: True if the user's input is valid, otherwise False

    >>> player_input = "2"
    >>> character_info =  {"name": "Anthony", "occupation": "Ninja", "location": (0, 0), "level": 1}
    >>> map_board = {(0, 0): "room1", (0, 1): "room2", (0, 2): "room3",(1, 0): "room4", (1, 1): "room5", (1,2): "room6"}
    >>> validate_movement(player_input, character_info, map_board)
    True
    >>> player_input = "3"
    >>> character_info =  {"name": "Momo", "occupation": "Samurai", "location": (0, 2), "level": 1}
    >>> map_board = {(0, 0): "room1", (0, 1): "room2", (0, 2): "room3",(1, 0): "room4", (1, 1): "room5", (1,2): "room6"}
    >>> validate_movement(player_input, character_info, map_board)
    False
    """
    current_location = list(character["location"])
    location_after_movement = current_location
    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1
    if tuple(location_after_movement) in board:
        return True
    else:
        return False


def move_character(user_input, character):
    """
    Move character based on the user input.

    :param user_input: a string
    :param character: a dictionary
    :precondition: user_input is a valid string ("1" for north, "3" for south, "4" for west, "2" for east)
    :precondition: character is a dictionary containing the character's location as a tuple (x, y)
    :postcondition: character's current location will be updated based on the user input

    >>> character_info = {"location": (0, 0)}
    >>> move_character("2", character_info)
    >>> character_info["location"]
    (1, 0)
    >>> character_info = {"location": (2, 0)}
    >>> move_character("3", character_info)
    >>> character_info["location"]
    (2, 1)
    """
    current_location = list(character["location"])
    location_after_movement = current_location

    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1

    character["location"] = tuple(location_after_movement)


def main():
    pass


if __name__ == "__main__":
    main()
