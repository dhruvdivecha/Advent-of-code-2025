with open('day4/input.txt') as f:
    lines = f.read().strip().split('\n')  

rows = len(lines)
cols = len(lines[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def count_neighbors(r, c, grid):
    count = 0
    for direction_x, direction_y in directions:
        nr = r + direction_x
        nc = c + direction_y
        
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                    count += 1

    return count


def partOne():
    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '@':
                neighbours = count_neighbors(r, c, lines)

                if neighbours < 4:
                    accessible += 1

    return accessible 


def partTwo():
    grid = [list(row) for row in lines]
    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbours = count_neighbors(r, c, grid)
                    if neighbours < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed
    
if __name__ == "__main__":
    print("Part One:", partOne())
    print("Part Two:", partTwo())


