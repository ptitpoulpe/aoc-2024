def parse_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(line.strip()) for line in file]
    return matrix

def get_element(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return matrix[row][col]
    return "O"

def find_element(matrix, value):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == value:
                return row, col
    return None

def turn_right(direction):
    match direction:
        case (-1, 0): # up
            return (0, 1) # right
        case (0, 1): # right
            return (1, 0) # down
        case (1, 0): # down
            return (0, -1) # left
        case (0, -1): # left
            return (-1, 0) # up

def print_matrix(matrix, done, block=None):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if get_element(matrix, row, col) == "^":
                print("^", end="")
            elif (row, col) in done:
                print("X", end="")
            elif (row, col) == block:
                print("@", end="")
            else:
                print(matrix[row][col], end="")
        print()

def path(matrix, row, col, direction, done=None, block=None):
    if done is None:
        done = set()
    current = (row, col, direction)
    while True:
        if current in done:
            return "Loop", done
        done.add(current)

        row, col, direction = current
        n_row, n_col = row + direction[0], col + direction[1]
        next_element = (
            "#" if (n_row, n_col) == block
            else get_element(matrix, n_row, n_col)
        )

        if next_element == "O":
            return "Out", done

        if next_element == "#":
            current = (row, col, turn_right(direction))
        else:
            current = (n_row, n_col, direction)

def part1(matrix):
    row, col = find_element(matrix, "^")
    direction = (-1, 0) # up
    #matrix[98][46] = "#"
    res, done = path(matrix, row, col, direction)
    #print(res)
    #print((98,46) in done)
    return len(set((row, col) for row, col, direction in done))

def part2(matrix):
    row, col = find_element(matrix, "^")
    direction = (-1, 0) # up
    loops = set()
    current = (row, col, direction)
    done = set()
    while True:
        row, col, direction = current
        n_row, n_col = row + direction[0], col + direction[1]
        next_element = get_element(matrix, n_row, n_col)

        if next_element == "O":
            break

        if next_element != "#" and (n_row, n_col) not in done:
            res, _ = path(
                matrix, row, col, direction,
                done.copy(), block=(n_row, n_col))
            if res == "Loop":
                loops.add((n_row, n_col))

        done.add((row, col))
        if next_element == "#":
            current = (row, col, turn_right(direction))
        else:
            current = (n_row, n_col, direction)
    return len(loops)

if __name__ == "__main__":
    print(f"Part1: {part1(parse_file('inputs/06.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/06.txt'))}")