with open("day2/input.txt") as f:
    data = f.read().strip().split(",")

def partOne(data):

    total_invalid_ids = 0

    for ids in data:

        start_id, end_id = ids.split("-")

        start_id = int(start_id)
        end_id = int(end_id)

        for id_num in range(start_id, end_id + 1):

            s = str(id_num)
            n = len(s)

            if n % 2 == 0:
                midpoint = n // 2

                first_half = s[:midpoint]
                second_half = s[midpoint:]

                if first_half == second_half:
                    total_invalid_ids += id_num

    return total_invalid_ids


def partTwo(data):
    
    total_invalid_ids = 0

    for ids in data:

        start_id, end_id = ids.split("-")

        start_id = int(start_id)
        end_id = int(end_id)

        for id_num in range(start_id, end_id + 1):
            
            s = str(id_num)
            n = len(s)

            for l in range(1, n):

                if n % l == 0:

                    pattern = s[:l]
                    repetitions = n // l

                    if pattern * repetitions == s:
                        total_invalid_ids += id_num
                        break
    return total_invalid_ids


if __name__ == "__main__":
    result = partOne(data)
    print(f"Part One: {result}")
    result = partTwo(data)
    print(f"Part Two: {result}")
                