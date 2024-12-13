import operator as op

def parse_file(file_path):
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            test_value, numbers = line.split(':')
            equations.append((
                int(test_value),
                list(map(int, numbers.strip().split())),
            ))
    return equations

class Equation:
    def __init__(self, result, values, ops):
        self.result = result
        self.values = values
        self.ops = ops

    def test(self, current, index):
        if  index == len(self.values):
            return current == self.result
        if current > self.result:
            return False
        for operator in self.ops:
            if self.test(
                    operator(current, self.values[index]),
                    index+1,
            ):
                return True
        return False

def part1(equations):
    sum_results = 0
    for result, values in equations:
        if Equation(
            result, values, [op.mul, op.add]
        ).test(values[0], 1):
            sum_results += result
    return sum_results

def part2(equations):
    sum_results = 0
    def concat(a, b):
        return int(str(a) +str(b))
    for result, values in equations:
        if Equation(
                result, values, [concat, op.mul, op.add]
        ).test(values[0], 1):
            sum_results += result
    return sum_results

if __name__=="__main__":
    print(f"Part1: {part1(parse_file('inputs/07.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/07.txt'))}")
