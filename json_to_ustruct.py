# Script to convert json to unreal engine 4 ustruct
import json


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


def create_struct_lines(struct):
    # return out_lines
    pass


def write_ustruct_file(ustruct_file, struct_lines):

    with open(ustruct_file, 'w') as f:
        # ustruct header first
        f.write("USTRUCT()\n")
        f.write("struct FJsonData\n")
        f.write("{\n")
        f.write("\tGENERATED_USTRUCT_BODY()\n\n")

        f.write(struct_lines)

        # close ustruct
        f.write("\n};")


def json_to_ustruct(json_file, ustruct_file):
    # convert json to python dict
    json_dict = json_to_dict(json_file)

    # for each key in the dictionary created from , determine the type of the value at that key
    for struct in json_dict:
        if type(json_dict[struct]) == "str":
            create_struct_lines(struct)
        elif type(json_dict[struct]) == "dict":
            # go another level deeper?
            pass
        elif type(json_dict[struct]) == "list":
          pass
        else:
            print("ERROR! Type was {}(expecting string or list).".format(str(type(json_dict[struct]))))

if __name__ == "__main__":
    json_to_ustruct("./02_nested/02_sample.json",
                    "./02_nested/sample.ustruct")
