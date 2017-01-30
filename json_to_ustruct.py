# make dict from json
# for key in json_dict
# if json_dict[key] is str
import json


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def json_to_dict(json_file):
    """
    Take in full filepath to json file, convert json to a python dict, and return that dict.
    :param json_file:
    :return:
    """
    # convert json file to dict
    with open(json_file, 'r') as in_file:
        json_dict = json.load(in_file)

    return json_dict


def process_struct(structs, json_dict):
    """
    Recursively process dictionary JSON objects to create USTRUCTS.
    :param structs: list all the structs seen as ('field_name', 'type') where field_name is value and type is str, etc
    :param json_dict: keys in dict created from JSON
    :return:
    """
    # for keys in dictonary of json object
    for key in json_dict:
        # if the value is a string, it can simply be added to the list of seen structs
        if type(json_dict[key]) == str:
            ustruct = (json_dict[key], 'str')
            structs.append(ustruct)

    print(structs)


if __name__ == "__main__":
    json_dict = json_to_dict("./02_nested/02_sample.json")
    process_struct([], json_dict)
