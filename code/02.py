
def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [
            [int(x) for x in line.strip().split()]
            for line in lines
            if line
        ]

def part1(lines):
    safe_reports = 0
    for line in lines:
        diffs = [
            r - l
            for r, l in zip(line[:-1], line[1:])
        ]
        if (all(0 < diff and diff <= 3 for diff in diffs) or
            all(-3 <= diff and diff < 0 for diff in diffs)):
            safe_reports += 1
    return safe_reports

def part2(lines):
    safe_reports = 0
    def test(line, order: int):
        diffs = [
            order * (r - l)
            for r, l in zip(line[:-1], line[1:])
        ]
        for i, diff in enumerate(diffs):
            if not (0 < diff and diff <= 3):
                return i
        return -1
    for line in lines:
        if (
                (asc := test(line, 1)) == -1 or
                test(line[:asc] + line[asc+1:], 1) == -1 or
                test(line[:asc+1] + line[asc+2:], 1) == -1 or
                (desc := test(line, -1)) == -1 or
                test(line[:desc] + line[desc+1:], -1) == -1 or
                test(line[:desc+1] + line[desc+2:], -1) == -1
        ):
            safe_reports += 1
    return safe_reports

if __name__ == "__main__":
    print(f"Part1: {part1(parse_file('inputs/02.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/02.txt'))}")
