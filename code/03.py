import re

def parse_file(file):
    with open(file, 'r') as f:
        return f.read()

def part1(data):
    return sum(
        int(l) * int(r)
        for l, r in re.findall(r"mul\((\d+),(\d+)\)", data)
    )

def part2(data):
    mul_enabled = True
    result = 0
    for m in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
        match m:
            case (l, r, "", ""):
                if mul_enabled:
                    result += int(l) * int(r)
            case ("", "", "do()", ""):
                mul_enabled = True
            case ("", "", "", "don't()"):
                mul_enabled = False
    return result

if __name__=="__main__":
    print(f"Part1: {part1(parse_file('inputs/03.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/03.txt'))}")