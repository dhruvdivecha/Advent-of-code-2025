with open("day7/input.txt") as f:
    grid = [line.strip() for line in f]

def partOne(grid):
    start_row, start_col = next((r, line.find('S')) for r, line in enumerate(grid) if 'S' in line)

    row = start_row + 1  
    col = start_col

    splits = 0
    beams = {(start_row + 1, start_col)} 

    while beams:
        new_beams = set()

        for row, col in beams:
            if row >= len(grid):
                continue 

            cell = grid[row][col]

            if cell == '^':
                splits += 1
                new_beams.add((row + 1, col - 1))
                new_beams.add((row + 1, col + 1))
            else:
                new_beams.add((row + 1, col))

        beams = new_beams  

    return splits

# had to use chatgpt to help with part two
def partTwo(grid):
    from functools import lru_cache

    start_row, start_col = next((r, line.find('S')) for r, line in enumerate(grid) if 'S' in line)

    @lru_cache(maxsize=None)
    def count_timelines(row, col):
        # If particle has moved off the grid
        if row >= len(grid):
            return 1

        cell = grid[row][col]

        if cell == '^':
            # Particle splits: count timelines for both left and right paths
            left = count_timelines(row + 1, col - 1) if col > 0 else 0
            right = count_timelines(row + 1, col + 1) if col < len(grid[0]) - 1 else 0
            return left + right
        else:
            # Particle continues straight down
            return count_timelines(row + 1, col)

    # Start one row below S
    total_timelines = count_timelines(start_row + 1, start_col)
    return total_timelines

if __name__ == "__main__":
    result_part_one = partOne(grid)
    print("Part One:", result_part_one)
    result_part_two = partTwo(grid)
    print("Part Two:", result_part_two)




