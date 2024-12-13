def parse_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(line.strip()) for line in file]
    return matrix

def get_element(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return matrix[row][col]
    return None

def get_indices(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            yield row, col

def get_neighbors(matrix, row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i, j) != (row, col) and 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                neighbors.append((i, j))
    return neighbors

def get_diagonal_neighbors(matrix, row, col):
    diagonal_neighbors = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            if 0 <= row + i < len(matrix) and 0 <= col + j < len(matrix[0]):
                diagonal_neighbors.append((row + i, col + j))
    return diagonal_neighbors

def part1(matrix):
    result = 0
    for x1, x2 in get_indices(matrix):
        if get_element(matrix, x1, x2) != "X":
            continue
        for m1, m2 in get_neighbors(matrix, x1, x2):
            if get_element(matrix, m1, m2) != "M":
                continue
            shift_1 = m1 - x1
            shift_2 = m2 - x2
            if (
                get_element(matrix, m1 + shift_1, m2 + shift_2) == "A" and
                get_element(matrix, m1 + shift_1 * 2, m2 + shift_2 * 2) == "S"
            ):
                result += 1
    return result

def part2(matrix):
    result = 0
    for a1, a2 in get_indices(matrix):
        if get_element(matrix, a1, a2) != "A":
            continue
        diags = get_diagonal_neighbors(matrix, a1, a2)
        ms = [
            (m1, m2)
            for m1, m2 in diags
            if get_element(matrix, m1, m2) == "M"
        ]
        if len(ms) != 2:
            continue
        if all(
            get_element(matrix, a1 - (m1 - a1), a2 - (m2 - a2)) == "S"
            for m1, m2 in ms
        ):
            result += 1
    return result




if __name__ == "__main__":
    print(f"Part1: {part1(parse_file('inputs/04.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/04.txt'))}")