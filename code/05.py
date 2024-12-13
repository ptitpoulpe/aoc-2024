from collections import defaultdict
from functools import cmp_to_key
from selectors import SelectSelector


def parse_file(file_path):
    with open(file_path, 'r') as file:
        p1, p2 = file.read().split("\n\n")
        p1 = [line.strip().split("|") for line in p1.split("\n")]
        p2 = [line.strip().split(",") for line in p2.split("\n") if line]
        return p1, p2

def part1(p1, p2):
    result = 0
    order = defaultdict(list)
    for r, l in p1:
        order[r].append(l)
    for line in p2:
        right_order = True
        for i, n in enumerate(line):
            if n in order and any(m in line[:i] for m in order[n]):
                right_order = False
                break
        if right_order:
            result += int(line[len(line)//2])
    return result

def part2(p1, p2):
    result = 0
    order = defaultdict(list)
    for r, l in p1:
        order[r].append(l)
    for line in p2:
        right_order = True
        for i, n in enumerate(line):
            if n in order and any(m in line[:i] for m in order[n]):
                right_order = False
                break
        if not right_order:
            line.sort(
                key=cmp_to_key(
                    lambda x, y: 0 if x == y else
                                 -1 if (x in order and y in  order[x]) else
                                 1
                )
            )
            result += int(line[len(line)//2])

    return result

if __name__ == "__main__":
    p1, p2 = parse_file('inputs/05.txt')
    #print(f"Part1: {part1(p1, p2)}")
    print(f"Part2: {part2(p1, p2)}")