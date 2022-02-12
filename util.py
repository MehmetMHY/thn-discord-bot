import datetime
import os
import json

with open("./config.json") as configfile:
    config = json.load(configfile)

def current_time():
    ctime = datetime.datetime.now()
    return {
        "second": ctime.second,
        "minute": ctime.minute,
        "hour": ctime.hour,
        "day": ctime.day,
        "month": ctime.month,
        "year": ctime.year
    }

def print_list(data):
    for line in data:
        print(line)

def read_file(name):
    with open(name) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def clean_fwords(data):
    data = list(set(data))

    new_data = []
    for word in data:
        if len(word) > 0:
            new_data.append(word.lower())
    
    return new_data

def get_file_paths(rpath, ftype):
    data = []
    for file in os.listdir(rpath):
        entry = {"path": "", "filename": ""}
        if ftype in file:
            entry["path"] = os.path.join(rpath, file)
            entry["filename"] = file
            data.append(entry)
    return data

def get_filter_words():
    filter_file_paths = get_file_paths(config["filter_words_path"], config["filter_word_file_ext"])

    orgfiler = {}
    for file in filter_file_paths:
        lines = read_file(file["path"])
        lines = clean_fwords(lines)

        key = str(file["filename"].split("_")[0])

        orgfiler[key] = lines

    return orgfiler

# https://www.geeksforgeeks.org/python-intersection-two-lists/
def list_intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [x for x in lst1 if x in temp]
    return lst3