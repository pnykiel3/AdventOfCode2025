def mul(list):
    result = 1
    for i in list:
        result *= i
    return result

def task():

    with open("input.data", 'r') as input_file:

        lines = [line.strip("\n") for line in input_file.readlines()]

    if not lines:
        return -1, -1
    
    operator_line = lines[-1]
    number_lines = lines[:-1]

    operations = operator_line.split()

    max_width = max(len(line) for line in number_lines)
    grid = [line.ljust(max_width) for line in number_lines]

    block_ranges = []
    start_col = 0

    #we are looking for blank columns to separate blocks
    for x in range(max_width + 1):
        is_separator = False
        if x == max_width:
            is_separator = True
        else:
            # Check if this column is empty across all rows
            col_is_empty = True
            for y in range(len(grid)):
                if grid[y][x] != ' ':
                    col_is_empty = False
                    break
            is_separator = col_is_empty

        if is_separator:
            # If we hit a separator and have accumulated a block, save it
            if x > start_col:
                block_ranges.append((start_col, x))
            start_col = x + 1
    
    result1 = 0
    result2 = 0

    for i, (start, end) in enumerate(block_ranges):
        if i >= len(operations): break
        op = operations[i]

        #Task 1
        numbers = []
        for row in grid:
            segment = row[start:end].split()
            for s in segment:
                numbers.append(int(s))
        result1 += sum(numbers) if op == '+' else mul(numbers)

        #Task 2
        numbers2 = []
        # Iterate columns strictly from Right to Left
        for col_idx in range(end - 1, start - 1, -1):
            # Build the number vertically
            digits = []
            for row_idx in range(len(grid)):
                char = grid[row_idx][col_idx]
                digits.append(char)
            
            num_str = "".join(digits).replace(" ", "")
            
            # If the column actually contained a number, parse it
            if num_str:
                numbers2.append(int(num_str))
                
        result2 += sum(numbers2) if op == '+' else mul(numbers2)

    return result1, result2
            






if __name__ == "__main__":
    r1, r2 = task()
    print("Task 1:", r1)
    print("Task 2:", r2)