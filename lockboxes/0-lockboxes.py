#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    unlocked = {0}
    to_check = [0]

    while to_check:
        box_index = to_check.pop()

        for key in boxes[box_index]:
            if 0 <= key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                to_check.append(key)

    return len(unlocked) == len(boxes)
