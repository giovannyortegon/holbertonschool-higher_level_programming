#!/usr/bin/python3
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []
my_list2 = []
if len(sys.argv) == 1:
    save_to_json_file(my_list, filename)
    print(my_list)
else:
    my_list = load_from_json_file(filename)
    if len(my_list) == 0:
        for idx in range(1, len(sys.argv)):
            my_list.append(sys.argv[idx])
        save_to_json_file(my_list, filename)
    else:
        my_list = load_from_json_file(filename)
        for idx in range(1, len(sys.argv)):
            my_list2.append(sys.argv[idx])
        my_list.extend(my_list2)
        save_to_json_file(my_list, filename)
    print(my_list)
