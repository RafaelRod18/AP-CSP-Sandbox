"""
General CodeQuest solution
J. Cihlar - January 2026
"""

import sys
import math
import string

def main() -> None:
    case_count: int = int(sys.stdin.readline().rstrip())
    for _ in range(case_count):
        color: str = str(input)
        case: str = sys.stdin.readline().rstrip() # you may need to tweak this depending on the problem
        color: str = color.lower
        # processing
        if color == "violet":
            print("In order to make violet, blue and red must be mixed.")
        elif color == "red-violet":
            print("In order to make red-violet, blue and red must be mixed.")
        elif color == "blue-violet":
            print("In order to make blue-violet, blue and red must be mixed.")
        elif color == "red":
            print("No colors need to be mixed to make red.")
        elif color == "yellow":
            print("No colors need to be mixed to make yellow.")
        elif color == "blue":
            print("No colors need to be mixed to make blue.")
        elif color == "green" or:
            print("In order to make green, blue and yellow must be mixed.")
        elif color == "blue-green":
            print("In order to make blue-green, blue and yellow must be mixed.")
        elif color == "yellow-green":
            print("In order to make yellow-green, blue and yellow must be mixed.")
        elif color == "ornage":
            print("In order to make orange, yellow and red must be mixed..")
        elif color == "yellow-orange":
            print("In order to make yellow-orange, yellow and red must be mixed.")
        elif color == "red-orange":
            print("In order to make red-orange, yellow and red must be mixed.")

        # output


if __name__ == "__main__":
    main()