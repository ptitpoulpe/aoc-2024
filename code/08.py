import itertools
from collections import defaultdict

def parse__file(file_path):
    with open(file_path, 'r') as file:
        antennas = defaultdict(list)
        rows = file.readlines()
        for r, row in enumerate(rows):
            for c, col in enumerate(row.strip()):
                if col != ".":
                    antennas[col].append((r, c))
    return (
        len(rows),
        len(row.strip()),
        antennas,
    )

def print_matrix(roms, cols, antennas, antinodes):
    print(sorted(antinodes))
    for r in range(rows):
        for c in range(cols):
            char = "."
            if (r, c) in antinodes:
                char = "#"
                antinodes.remove((r, c))
            else:
                for antenna, positions in antennas.items():
                    if (r, c) in positions:
                        positions.remove((r, c))
                        char = antenna
                        break
            print(char, end="")
        print()
    print(antinodes)
    print(antennas)

def part1(rows, cols, antennas):
    result = set()
    for antenna, positions in antennas.items():
        for (x1, y1), (x2, y2) in itertools.combinations(positions, 2):
            xs = x2 - x1
            ys = y2 - y1
            nx1 = x1 - xs
            ny1 = y1 - ys
            nx2 = x2 + xs
            ny2 = y2 + ys
            if (
                0 <= nx1 and nx1 < rows and
                0 <= ny1 and ny1 < cols
            ):
                result.add((nx1, ny1))
            if (
                0 <= nx2 and nx2 < rows and
                0 <= ny2 and ny2 < cols
            ):
                result.add((nx2, ny2))
    return len(result)

def part2(rows, cols, antennas):
    result = set()
    for antenna, positions in antennas.items():
        for (x1, y1), (x2, y2) in itertools.combinations(positions, 2):
            xs = x2 - x1
            ys = y2 - y1
            nx1 = x1
            ny1 = y1

            while (
                0 <= nx1 and nx1 < rows and
                0 <= ny1 and ny1 < cols
            ):
                result.add((nx1, ny1))
                nx1 -= xs
                ny1 -= ys

            nx2 = x2
            ny2 = y2
            while (
                0 <= nx2 and nx2 < rows and
                0 <= ny2 and ny2 < cols
            ):
                result.add((nx2, ny2))
                nx2 += xs
                ny2 += ys

    return len(result)

if __name__=="__main__":
    rows, cols, antennas = parse__file('inputs/08.txt')
    print(f"Part1: {part1(rows, cols, antennas)}")
    print(f"Part2: {part2(rows, cols, antennas)}")