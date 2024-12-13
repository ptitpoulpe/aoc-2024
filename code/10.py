def parse_file(file_path):
    with open(file_path, 'r') as file:
        return [
            [int(char) for char in line.strip()]
            for line in file.readlines()
        ]

def find_all_elements(matrix, value):
    indices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == value:
                indices.append((row, col))
    return indices

def reach_end(matrix, x, y, current):
    if current == 9:
        yield (x, y)
    for sx, sy in (
        (s, 0) if is_x else (0, s)
        for s in [-1, 1]
        for is_x in [True, False]
    ):
        nx = x + sx
        ny = y + sy
        if (nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]) or
                matrix[nx][ny] != current + 1):
            continue
        yield from reach_end(matrix, nx, ny, current + 1)

def part1(matrix):
    result = 0
    for x1, x2 in find_all_elements(matrix, 0):
        result += len(set(reach_end(matrix, x1, x2, 0)))
    return result

def part2(matrix):
    result = 0
    for x1, x2 in find_all_elements(matrix, 0):
        result += len(list(reach_end(matrix, x1, x2, 0)))
    return result

if __name__=="__main__":
    print(f"Part1: {part1(parse_file('inputs/10.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/10.txt'))}")