
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": 0,
            "first_name": "John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers": [7, 13, 22],
        },
        {
            "id": 1,
            "first_name": "Jane",
            "last_name": "Jackson",
            "age": 35,
            "lucky_numbers": [10, 14, 3],
        },
        {
            "id": 2,
            "first_name": "Jimmy",
            "last_name": "Jackson",
            "age": 5,
            "lucky_numbers": [1],
        },
        ]

    member = {
        "id": int,
        "first_name": "",
        "last_name": "Jackson",
        "age": int,
        "lucky_numbers": [],
    }

    # read-only: Use this method to generate random members ID's when adding members into the list
    def generate_Id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member["id"] is None:
            member["id"] = self.generate_Id()
        self._members.append(member)
        # fill this method and update the return
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
