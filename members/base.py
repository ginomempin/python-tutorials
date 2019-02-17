"""Accesses member information."""

import json
from difflib import get_close_matches


def _get_member_list():
    try:
        members = dict()
        with open("members.json", "r") as members_file:
            members = json.load(members_file)
        return members
    except IOError:
        return False


member_list = _get_member_list()
if not member_list:
    print("ABORT. Cannot load data file.")
else:
    name = input("Enter name: ")
    member = member_list.get(name.lower())
    if member:
        for field, info in member.items():
            print("{0:<11} : {1:<}".format(field, info))
    else:
        print("There is no entry for '" + name + "'.")
        possibles = get_close_matches(name, member_list.keys(), n=5, cutoff=0.75)
        if possibles:
            print("Did you mean:")
            for p in possibles:
                print("  {}?".format(p))
