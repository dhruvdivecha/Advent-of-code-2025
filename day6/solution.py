from functools import reduce


with open('day6/input.txt') as f:
    lines = f.read().strip().split('\n')
    data_lines = lines[:-1]    
    operator_line = lines[-1].strip()

    numbers = [list(map(int, line.split())) for line in data_lines]
    operators = list(operator_line.split())  

    
def solve(op, *values):
    if op == '+':
        return sum(values)
    elif op == '-':
        return reduce(lambda a, b: a - b, values)
    elif op == '*':
        return reduce(lambda a, b: a * b, values)
    elif op == '/':
        return reduce(lambda a, b: a / b, values)
    else:
        raise ValueError(f"Unknown operator: {op}")


def partOne(numbers, operators):
    num_cols = len(numbers[0])
    result = 0

    for i in range(num_cols):
        column_values = [row[i] for row in numbers]  
        op = operators[i]                             
        
        result += solve(op, *column_values)
    return result

def partTwo(raw_lines):
    max_len = max(len(line) for line in raw_lines)
    grid = [line.ljust(max_len) for line in raw_lines]
    
    num_rows = len(grid) - 1
    num_cols = max_len
    operator_row = grid[-1]
    
    result = 0
    current_numbers = []
    current_op = None
    
    for col in range(num_cols - 1, -1, -1):
        op_char = operator_row[col]
        is_separator = all(grid[row][col] == ' ' for row in range(num_rows))
        
        if is_separator:
            if current_numbers and current_op:
                result += solve(current_op, *current_numbers)
            current_numbers = []
            current_op = None
        else:
            if op_char in ['+', '-', '*', '/']:
                current_op = op_char
            
            digits = ''
            for row in range(num_rows):
                char = grid[row][col]
                if char.isdigit():
                    digits += char
            
            if digits:
                current_numbers.append(int(digits))
    
    if current_numbers and current_op:
        result += solve(current_op, *current_numbers)
    
    return result
    
    
if __name__ == "__main__":
    result = partOne(numbers, operators)
    print(result)   
    result = partTwo(lines)
    print(result) 

