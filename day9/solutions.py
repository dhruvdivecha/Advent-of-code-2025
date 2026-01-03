from collections import deque

def load_input():
    with open('day9/input.txt') as f:
        data = [line.strip() for line in f if line.strip()]
    return data

# --- Part 1 ---
def parse(data):
    return [(int(x), int(y)) for x, y in (line.split(',') for line in data)]

def part1(data):
    points = parse(data)
    max_area = 0

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)

    return max_area

# --- Part 2 --- ( Had to use chatgtp to help with this part )
def part2(data):
    points = parse(data)

    # Coordinate compression
    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})

    # Build scaled grid
    grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]
    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
        for cx in range(cx1, cx2 + 1):
            for cy in range(cy1, cy2 + 1):
                grid[cx][cy] = 1

    # Flood-fill from outside
    outside = {(-1, -1)}
    queue = deque(outside)
    while queue:
        tx, ty = queue.popleft()
        for nx, ny in [(tx-1, ty), (tx+1, ty), (tx, ty-1), (tx, ty+1)]:
            if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]): continue
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1: continue
            if (nx, ny) in outside: continue
            outside.add((nx, ny))
            queue.append((nx, ny))

    # Fill interior
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in outside:
                grid[x][y] = 1

    # Build prefix sum array
    psa = [[0] * len(grid[0]) for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            left = psa[x-1][y] if x > 0 else 0
            top = psa[x][y-1] if y > 0 else 0
            topleft = psa[x-1][y-1] if x > 0 and y > 0 else 0
            psa[x][y] = left + top - topleft + grid[x][y]

    # Rectangle validity check
    def valid(x1, y1, x2, y2):
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
        left = psa[cx1-1][cy2] if cx1 > 0 else 0
        top = psa[cx2][cy1-1] if cy1 > 0 else 0
        topleft = psa[cx1-1][cy1-1] if cx1 > 0 and cy1 > 0 else 0
        count = psa[cx2][cy2] - left - top + topleft
        return count == (cx2 - cx1 + 1) * (cy2 - cy1 + 1)

    # Compute largest rectangle
    max_area = max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for i, (x1, y1) in enumerate(points)
        for x2, y2 in points[:i]
        if valid(x1, y1, x2, y2)
    )

    return max_area

# --- Main ---
if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
