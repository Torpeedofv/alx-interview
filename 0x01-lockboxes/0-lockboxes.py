#!/usr/bin/python3
"""A module for a function canUnlockAll to
determine if all boxescan be opened"""


def canUnlockAll(boxes):
    """A function to determin if all boxes can be opened"""
    allBoxes = len(boxes)
    alreadyOpend = [False] * allBoxes
    alreadyOpend[0] = True
    queue = [0]

    while queue:
        present_box = queue.pop(0)
        keys = boxes[present_box]

        for key in keys:
            if key < allBoxes and not alreadyOpend[key]:
                alreadyOpend[key] = True
                queue.append(key)

    return all(alreadyOpend)
