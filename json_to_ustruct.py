# Script to convert json to unreal engine 4 ustruct
import json


def json_to_ustruct(json_file, ustruct_file):
    # convert json file to dict
    with open(json_file, 'r') as in_file:
        json_dict = json.load(in_file)

    with open(ustruct_file, 'w') as out_file:
        # open FJsonData ustruct
        out_file.write("USTRUCT()\n")
        out_file.write("struct FJsonData\n")
        out_file.write("{\n")
        out_file.write("\tGENERATED_USTRUCT_BODY()\n\n")
        # a key is an FString
        for item in json_dict:
            out_file.write("\tUPROPERTY()\n")
            out_file.write("\tFString {};".format(item))
        # close FJsonData ustruct
        out_file.write("\n};")

if __name__ == "__main__":
    json_to_ustruct("./01_single_key_value/01_sample.json",
                    "./01_single_key_value/sample.ustruct")
