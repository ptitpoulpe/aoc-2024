def parse_file(file_path):
    with open(file_path, 'r') as file:
        return [int(char) for char in file.read().strip()]

def part1(data):
    file = True
    blocks = []
    ids = 0
    for number in data:
        blocks.append([file, ids, number])
        if file:
            ids += 1
        file = not file
    result = 0
    pos = 0
    while blocks:
        lfile, lnumber, lcount = blocks[0]
        if lcount == 0:
            blocks.pop(0)
            continue
        if lfile:
            #print(f"lnumber: {lnumber}, pos: {pos}")
            result += lnumber * pos
            blocks[0][2] -= 1
            if lcount == 0:
                print("Error1")
        else:
            rfile, rnumber, rcount = blocks[-1]
            if rcount == 0:
                blocks.pop()
                continue
            if rfile:
                #print(f"rnumber: {rnumber}, pos: {pos}")
                result += rnumber * pos
                blocks[0][2] -= 1
                if lcount == 0:
                    print("Error1")
                blocks[-1][2] -= 1
                if rcount == 0:
                    print("Error1")
            else:
                blocks.pop()
                continue
        pos += 1
    return result

def part2(data):
    file = True
    blocks = []
    ids = 0
    for number in data:
        blocks.append([file, ids, number])
        if file:
            ids += 1
        file = not file
    pos = len(blocks) - 1
    while pos >= 0:
        rfile, rnumber, rcount = blocks[pos]
        if not rfile:
            pos -= 1
            continue
        found = False
        for i, (lfile, lnumber, lcount) in enumerate(blocks):
            if i == pos:
                break
            if not lfile and rcount <= lcount:
                found = True
                break
        if found:
            #print(f"found for {(pos, rfile, rnumber, rcount)} in "
            #      f"{(i, lfile, lnumber, lcount)}")
            blocks[i][2] -= rcount
            if blocks[i][2] == 0:
                #print("pop")
                blocks.pop(i)
                pos -=1
            blocks.insert(i, (rfile, rnumber, rcount))
            pos += 1
            blocks[pos] = (False, rnumber, rcount)
        pos -= 1
        #print(blocks)
    pos = 0
    result = 0
    for file, number, count in blocks:
        if file:
            for i in range(count):
                result += number * pos
                pos += 1
        else:
            pos += count

    return result

if __name__ == "__main__":
    print(f"Part1: {part1(parse_file('inputs/09.txt'))}")
    print(f"Part2: {part2(parse_file('inputs/09.txt'))}")