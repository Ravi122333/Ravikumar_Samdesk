"""
Advent of Code 2024 - Day 2: Red-Nosed Reports (Part 1)

Problem:
We are given multiple reports. Each report contains numbers (levels).
We need to determine how many reports are "safe".

A report is SAFE if:
1. Levels are strictly increasing OR strictly decreasing
2. Adjacent differences are between 1 and 3 (inclusive)

Author: (Your Name)
Language: Python 3
"""

# ------------------ CORE LOGIC ------------------

def is_safe_report(levels):
    """
    Check whether a single report is safe or not.
    
    Args:
        levels (list): list of integers representing one report

    Returns:
        bool: True if safe, False otherwise
    """

    # Assume both conditions are true at the start
    is_increasing = True
    is_decreasing = True

    # Check each adjacent pair
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        # Rule 1: difference must be between 1 and 3
        if abs(diff) < 1 or abs(diff) > 3:
            return False  # invalid step size

        # Check direction
        if diff > 0:
            is_decreasing = False
        elif diff < 0:
            is_increasing = False

    # Safe only if one consistent direction exists
    return is_increasing or is_decreasing


# ------------------ PROCESS INPUT ------------------

def count_safe_reports(reports):
    """
    Count how many reports are safe.

    Args:
        reports (list of str): raw input lines

    Returns:
        int: number of safe reports
    """

    safe_count = 0

    for line in reports:
        # Convert string line → list of integers
        levels = list(map(int, line.split()))

        # Check safety
        if is_safe_report(levels):
            safe_count += 1

    return safe_count


# ------------------ MAIN EXECUTION ------------------

if __name__ == "__main__":

    # Read input from file (recommended for GitHub / AoC)
    # Save your puzzle input in: input.txt
    with open("input.txt", "r") as file:
        reports = file.read().strip().split("\n")

    result = count_safe_reports(reports)

    print("Safe reports:", result)