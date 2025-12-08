with open('day5/input.txt') as f:
    lines = f.read().strip().split('\n')
    idx = lines.index('')
    range_lines = lines[:idx]
    id_lines = lines[idx+1:]


def partOne(range_lines, id_lines):
    ranges = []
    ids = [int(x) for x in id_lines]
    spoiled = 0
    fresh = 0

    for r in range_lines:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))

    for id_value in ids:
        isFresh = False

        for start, end in ranges:
            if start <= id_value <= end:
                isFresh = True
                fresh += 1
                break

        if not isFresh:
            spoiled += 1

    return fresh


def partTwo(range_lines):
    ranges = []
    fresh = 0

    for r in range_lines:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))

    ranges.sort()
    current_start, current_end = ranges[0]
    
    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)

        else:
            fresh += (current_end - current_start + 1)
            current_start, current_end = start, end

    fresh += (current_end - current_start + 1)
    return fresh 
    

if __name__ == "__main__":
    result = partOne(range_lines, id_lines)
    print(result)
    result = partTwo(range_lines)
    print(result)