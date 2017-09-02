"""Accesses member information."""

import json


def _getMembers():
    try:
        dataFile = open("data.json", "r")
        data = json.load(dataFile)
        return data
    except IOError:
        return False


index = _getMembers()
if isinstance(index, dict):
    key = input("Enter key: ")
    val = index.get(key)
    if val is not None:
        print(val)
    else:
        print("There is no entry for '" + key + "'")
else:
    print("ABORT. Cannot load data file.")
