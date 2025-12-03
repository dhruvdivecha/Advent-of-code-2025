with open ('day3/input.txt') as f:
    lines = f.read().strip().split('\n')

def partOne(lines):
    total_joltage = 0

    for line in lines:
        max_bank_joltage = 0
        n = len(line)

        for i in range(n -1):

            for j in range(i + 1, n):

                first = str(line[i])
                second = str(line[j])

                joltage = first + second
                joltage = int(joltage)

                if joltage > max_bank_joltage:
                    max_bank_joltage = joltage

        total_joltage += max_bank_joltage

    return total_joltage

def partTwo(lines):
    total_joltage = 0
    length = 12

    for line in lines:
        n = len(line)

        d = n - length

        result = []

        for digit in line: 
            while d > 0 and result and digit > result[-1]:
                result.pop()
                d -= 1
        
            result.append(digit)

        final_result = result[:length]

        joltage_str = "".join(final_result)
        joltage = int(joltage_str)
        total_joltage += joltage

    return total_joltage


if __name__ == "__main__":
    result_part_one = partOne(lines)
    print("Part One:", result_part_one)
    result_part_two = partTwo(lines)
    print("Part Two:", result_part_two)