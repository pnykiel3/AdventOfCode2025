import re

def task1():
    output = 0
    mins = []
    maxs = []
    re_pattern = r'(\d+)-(\d+)'
    with open("input.data", 'r') as input_file:
        for line in input_file:
            if line.strip() == "":
                continue
            match = re.match(re_pattern, line.strip())
            if match:
                mins.append(int(match.group(1)))
                maxs.append(int(match.group(2)))
            else:
                number = int(line.strip())
                for min_v, max_v in zip(mins, maxs):
                    if min_v <= number <= max_v:
                        output += 1
                        break
        
    ranges = sorted(zip(mins, maxs))
    current_start, current_end = ranges[0]
    output2 = 0
    new_ranges = []

    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            new_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    new_ranges.append((current_start, current_end))

    for i in new_ranges:
        output2 += i[1] - i[0] + 1

# 1-5   3-7 -> 1-7
# 1-7 7-10 -> 1 - 10


                    
    return output, output2

if __name__ == "__main__":
    result1, result2 = task1()
    print("Task 1:", result1)
    print("Task 2:", result2)