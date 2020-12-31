import json

def getFile():
    with open('./cyberStarter.json') as f:
        data = json.load(f)

    return data