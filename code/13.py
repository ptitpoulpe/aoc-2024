import re

def parse_file(file_path):
    with (open(file_path, 'r') as file):
        return [
            [int(x) for x in prob]
            for prob in re.findall(r"""
                Button\ A:\ X\+(\d+),\ Y\+(\d+)\n
                Button\ B:\ X\+(\d+),\ Y\+(\d+)\n
                Prize:\ X=(\d+),\ Y=(\d+)
                """,
                file.read(),
                re.VERBOSE,
            )
        ]

def solve(problems):
    result = 0
    for ax, ay, bx, by, px, py in problems:
        # find a and b for which:
        # ax * a + bx * b = px
        # ay * a + by * b = py
        a = (px * by - py * bx) / (ax * by - ay * bx)
        b = (px - ax * a) / bx
        if a.is_integer() and b.is_integer():
            result += a*3 + b
    return int(result)

def part1(problems):
    return solve(problems)

def part2(problems):
    conv = 10000000000000
    return solve(
        (ax, ay, bx, by, px + conv, py + conv)
        for ax, ay, bx, by, px, py in problems
    )

if __name__=="__main__":
    print(f"Part1: {part1(parse_file('inputs/13.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/13.txt'))}")