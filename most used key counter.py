# most used character counter takes a file and counts how many times all special and number characters occur
# the special characters and numbers are counted separately giving each both their own percentage out of 100

# this can be used for whatever characters you want to check just specify the path of the file u want to check in file_path
# and add another, or edit an existing 2D array following this format [{"character": "&", "count": 0}], then call
# mostUsedCharactersCounter("char group name", array) passing in a string with a name of the character group and a 2D array

from audioop import reverse


file_path = "file combiner output.txt"

symbols_array = [
    {"character": "!", "count": 0},
    {"character": "@", "count": 0},
    {"character": "#", "count": 0},
    {"character": "$", "count": 0},
    {"character": "%", "count": 0},
    {"character": "^", "count": 0},
    {"character": "&", "count": 0},
    {"character": "*", "count": 0},
    {"character": "(", "count": 0},
    {"character": ")", "count": 0},
    {"character": "-", "count": 0},
    {"character": "_", "count": 0},
    {"character": "=", "count": 0},
    {"character": "+", "count": 0},
    {"character": "[", "count": 0},
    {"character": "{", "count": 0},
    {"character": "]", "count": 0},
    {"character": "}", "count": 0},
    {"character": "\\", "count": 0},
    {"character": "|", "count": 0},
    {"character": ";", "count": 0},
    {"character": ":", "count": 0},
    {"character": "'", "count": 0},
    {"character": '"', "count": 0},
    {"character": "<", "count": 0},
    {"character": ",", "count": 0},
    {"character": ">", "count": 0},
    {"character": ".", "count": 0},
    {"character": "/", "count": 0},
    {"character": "?", "count": 0}
]

numbers_array = [
    {"character": "1", "count": 0},
    {"character": "2", "count": 0},
    {"character": "3", "count": 0},
    {"character": "4", "count": 0},
    {"character": "5", "count": 0},
    {"character": "6", "count": 0},
    {"character": "7", "count": 0},
    {"character": "8", "count": 0},
    {"character": "9", "count": 0},
    {"character": "0", "count": 0}
]


def mostUsedCharactersCounter(character_group_name, array):

    file = open(file_path, "r")

    # loop to count occurrences of characters in a file
    total_amount = 0
    for line in file:
        for char in line:
            for item in array:
                if item["character"] == char:
                    item["count"] += 1
                    total_amount += 1

    # sorts array by count and reverses order to highest-lowest
    array.sort(key=lambda item: item.get("count"), reverse=True)

    print(f"\n\n{character_group_name}")

    # calculates a percentage and prints a message if item is greater than 0
    for item in array:
        if item["count"] != 0:
            percent = (item["count"]/total_amount)*100
            print(
                f'{item["character"]} occurred {item["count"]} times at {percent:.2f}%')
    file.close()


# these are an example u can delete these and use your own
mostUsedCharactersCounter("SYMBOLS", symbols_array)
mostUsedCharactersCounter("NUMBERS", numbers_array)
