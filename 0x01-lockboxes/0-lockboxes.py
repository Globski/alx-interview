#!/usr/bin/python3
"""Solution to lockboxes problem"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
    boxes (list): A list of lists where each inner list contains
                  keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    visited = set()
    queue = [0]

    while queue:
        box_index = queue.pop(0)
        if box_index not in visited:
            visited.add(box_index)

            for key in boxes[box_index]:
                if key not in visited and key < len(boxes):
                    queue.append(key)

    return len(visited) == len(boxes)
