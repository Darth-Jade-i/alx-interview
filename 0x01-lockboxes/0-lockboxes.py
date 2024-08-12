#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    determines if all boxes can be opened
    """
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box (box 0)

    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            # Add all keys in the current box to the stack if valid boxes
            for key in boxes[current_box]:
                if key < n and key not in visited:
                    stack.append(key)

    # return True if visited boxes is equal to the total number of boxes
    return len(visited) == n


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
