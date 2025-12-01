with open("day1/input.txt") as f:
    rotations = f.read().strip().split("\n")


def partOne():
    zero_count = 0
    current_position = 50

    for rotation in rotations:
        direction = rotation[0]
        value = int(rotation[1:])
        
        if direction == "L":
            current_position -= value
        elif direction == "R":
            current_position += value
        
        current_position = current_position % 100
        
        if current_position == 0:
            zero_count += 1

    print("password:", zero_count)   
     

def partTwo():
    zero_count = 0
    current_position = 50

    for rotation in rotations:
        direction = rotation[0]
        value = int(rotation[1:])

        step = -1 if direction == "L" else 1

        for _ in range(value):
            current_position = (current_position + step) % 100
            if current_position == 0:
                zero_count += 1

    print("password:", zero_count)


if __name__ == "__main__":
    partOne()
    partTwo()
