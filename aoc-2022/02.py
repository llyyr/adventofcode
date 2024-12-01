#!/usr/bin/env python3.11

def main(part):
    if part == 1:
        MAP = {
                "A X": 1+3, "A Y": 2+6, "A Z": 3+0,
                "B X": 1+0, "B Y": 2+3, "B Z": 3+6,
                "C X": 1+6, "C Y": 2+0, "C Z": 3+3,
                }
    elif part == 2:
        MAP = {
                "A X": 3+0, "A Y": 1+3, "A Z": 2+6,
                "B X": 1+0, "B Y": 2+3, "B Z": 3+6,
                "C X": 2+0, "C Y": 3+3, "C Z": 1+6,
                }
    print(sum(MAP[x.strip()] for x in open('02.txt')))

main(1)
main(2)
