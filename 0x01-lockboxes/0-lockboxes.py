#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
    boxes (list): A list of lists where each inner list contains
                  keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
