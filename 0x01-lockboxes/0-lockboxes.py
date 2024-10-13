#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list): A list of lists where each inner list contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    from collections import deque

    visited = set()
    queue = deque([0])

    while queue:
        box_index = queue.popleft()
        if box_index not in visited:
            visited.add(box_index)
            for key in boxes[box_index]:
                if key not in visited and key < len(boxes):
                    queue.append(key)

    return len(visited) == len(boxes)
