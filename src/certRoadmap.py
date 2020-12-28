import json

def getMapInfo(name):
    with open('./roadmap.json') as f:
        data = json.load(f)

    maps = data["maps"]

    if name == "all":
        return maps
    
    for map in maps:
        if name == map["shortname"]:
            return map

    return False

def getCerts(map_name):
    with open('./roadmap.json') as f:
        data = json.load(f)

    certs = data["certs"]
    ret = []

    for cert in certs:
        if map_name in cert["plans"]:
            ret.append(cert)

    return ret

def getCertInfo(name):
    with open('./roadmap.json') as f:
        data = json.load(f)

    certs = data["certs"]
    
    for cert in certs:
        if name.lower() in cert["name"].lower():
            return cert
        
    return False