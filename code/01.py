from collections import Counter


def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return list(zip(*(
            [int(x) for x in line.strip().split()]
            for line in lines
            if line
        )))

def part1(columns):
    return sum(
        abs(l - r)
        for l, r  in zip(*(
            sorted(column)
            for column in columns
        ))
    )

def part2(columns):
    left, right = columns
    # count the numbers of occurences of each number in each column
    counts = Counter(right)
    return sum(
        l * counts[l]
        for l in left
    )

if __name__ == "__main__":
    print(f"Part1: {part1(parse_file('inputs/01.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/01.txt'))}")

