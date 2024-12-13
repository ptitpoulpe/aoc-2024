from collections import defaultdict


def parse__file(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def area(group):
    return len(group)

def perimeter(group):
    result = 0
    for x, y in group:
        for sx, sy in (
            (s, 0) if is_x else (0, s)
            for s in [-1, 1]
            for is_x in [True, False]
        ):
            if (x + sx, y + sy) not in group:
                result += 1
    return result

def perimeter_discount(group):
    xps = defaultdict(list)
    yps = defaultdict(list)
    for x, y in group:
        for sx in [-1, 1]:
            if (x + sx, y) not in group:
                xps[x + (sx/4)].append(y)
        for sy in [-1, 1]:
            if (x, y + sy) not in group:
                yps[y + (sy/4)].append(x)
    result = 0
    for x, ys in xps.items():
        ys.sort()
        result += 1
        for y1, y2 in zip(ys, ys[1:]):
            if y2 != y1 + 1:
                result += 1
    for y, xs in yps.items():
        xs.sort()
        result += 1
        for x1, x2 in zip(xs, xs[1:]):
            if x2 != x1 + 1:
                result += 1
    return result

def compute(matrix, perimeter_func):
    todo = {
        (x, y)
        for x in range(len(matrix))
        for y in range(len(matrix[x]))
    }
    groups = []
    while todo:
        current = todo.pop()
        current_value = matrix[current[0]][current[1]]
        current_group = []
        todo_neighbors = [current]
        while todo_neighbors:
            x, y = todo_neighbors.pop()
            current_group.append((x, y))
            for sx, sy in (
                    (s, 0) if is_x else (0, s)
                    for s in [-1, 1]
                    for is_x in [True, False]
            ):
                nx = x + sx
                ny = y + sy
                if (nx, ny) in todo and matrix[nx][ny] == current_value:
                    todo_neighbors.append((nx, ny))
                    todo.remove((nx, ny))
        groups.append((current_value,current_group))
    return sum(
        area(group) * perimeter_func(group)
        for value, group in groups
    )

def part1(matrix):
    return compute(matrix, perimeter)

def part2(matrix):
    return compute(matrix, perimeter_discount)

if __name__ == "__main__":
    print(f"Part1: {part1(parse__file('inputs/12.txt'))}")
    print(f"Part2: {part2(parse__file('inputs/12.txt'))}")
