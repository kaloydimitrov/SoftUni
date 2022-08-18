# --------------------------------------------------------------------------------------------   01. String Game

string = input()

command = input()

while command != "Done":
    data = command.split(" ")
    action = data[0]

    if action == "Change":
        char_one = data[1]
        replacement = data[2]

        string = string.replace(char_one, replacement)

        print(string)

    elif action == "Includes":
        substring_one = data[1]

        if substring_one in string:
            print("True")
        else:
            print("False")

    elif action == "End":
        substring = data[1]

        true_or_false = string.endswith(substring)

        print(true_or_false)

    elif action == "Uppercase":
        string = string.upper()

        print(string)

    elif action == "FindIndex":
        char = data[1]

        index = string.index(char)
        print(index)

    elif action == "Cut":
        first_index = int(data[1])
        count = int(data[2])

        string = string[first_index:first_index + count]

        print(string)

    command = input()

# --------------------------------------------------------------------------------------------   02. Boss Rush

import re

count = int(input())

regex = r"\|([A-Z]+)\|:#([A-Za-z]+ [A-Za-z]+)#"

for _ in range(count):
    current_input = input()
    true_or_false = bool(re.match(regex, current_input))

    if true_or_false:
        data = re.findall(regex, current_input)
        name = data[0][0]
        title = data[0][1]

        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")

    else:
        print("Access denied!")

# --------------------------------------------------------------------------------------------   03. Dictionary

words_definitions = input().split(" | ")
dictinary = {}

for word_definition in words_definitions:
    data = word_definition.split(": ")
    key = data[0]
    value = data[1]

    if key not in dictinary:
        dictinary[key] = [value]
    else:
        dictinary[key].append(value)

test_words = input().split(" | ")

command = input()
if command == "Test":
    for word in test_words:
        if word in dictinary.keys():
            print(word + ":")
            for definition in dictinary[word]:
                print(f" -{definition}")

elif command == "Hand Over":
    for key in dictinary.keys():
        print(key, end=" ")
