from functools import cache


def parse_file(file_path):
    with open(file_path, 'r') as file:
        return [
            number
            for number in file.read().strip().split()
        ]

@cache
def blink(number, blinks):
    if blinks == 0:
        return 1
    if number == "0":
        return blink("1", blinks - 1)
    if len(number) % 2 == 0:
        middle = len(number) // 2
        return (
            blink(number[:middle], blinks - 1) +
            blink(str(int(number[middle:])), blinks - 1)
        )
    return blink(str(int(number) * 2024), blinks - 1)

def part1(numbers):
    return sum(
        blink(number, 25)
        for number in numbers
    )

def part2(numbers):
    return sum(
        blink(number, 75)
        for number in numbers
    )

if __name__ == "__main__":
    numbers = parse_file('inputs/11.txt')
    print(f"Part1: {part1(numbers)}")
    print(f"Part2: {part2(numbers)}")