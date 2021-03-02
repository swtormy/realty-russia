import json


def getRGID(name):
    with open('rgid.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        

    for rgid in data['subtree']:

        if name.lower() in rgid['name'].lower():
            return rgid['rgid']
    return "Sorry, it's name not found"


