def task1():
    output = 0
    with open("input.data", 'r') as input_file:
        for line in input_file:
            # Strip whitespace/newline characters from the line
            line = line.strip()
            # If the line is too short to form a 2-digit number, skip it
            if len(line) < 2:
                continue
            
            # Search for the best tens digit from 9 down to 1
            # This loop finds the first occurrence of the highest possible tens
            # digit. Once found, we pick the maximum digit that appears after it
            # to be the units digit.
            for tens_val in range(9, 0, -1):
                tens_char = str(tens_val)

                # Find the first occurrence of this digit in the line
                idx = line.find(tens_char)

                # line.find returns -1 if not found. Also require that this
                # occurrence is not the last character (so we can pick a units digit)
                if idx != -1 and idx < len(line) - 1:

                    # take everything after the found tens digit
                    remainder = line[idx+1:]

                    # We assume the input contains only digit characters; using
                    # max() on the substring returns the largest digit (as a char)
                    best_unit = max(remainder)

                    # Compose the two-digit number and add to the running total
                    number = int(tens_char + best_unit)
                    output += number

                    # Found the best pair for this line — break to process next line
                    break
                    
    return output


def task2():
    output = 0
    with open("input.data", 'r') as input_file:
        for line in input_file:
            # Trim newline/whitespace
            line = line.strip()
            # Expect at least 12 characters for this task; otherwise skip
            if len(line) < 12:
                continue

            current_number = ""
            current_search_area = line

            # For each remaining slot (from 11 down to 0) find the
            # highest digit available in the remaining search area. This
            # greedily builds a number by choosing the largest possible next
            # digit while preserving order.
            # Note: algorithm assumes input digits are characters '0'..'9'.
            for remain in range(11, -1, -1):
                for digit_value in range(9, -1, -1):
                    digit_char = str(digit_value)
                    idx = current_search_area.find(digit_char)
                    # idx < len(current_search_area) - remain ensures there
                    # will still be enough characters left after taking this
                    # digit to fill the remaining slots.
                    if idx != -1 and idx < len(current_search_area) - remain:
                        # move the search window after the chosen digit
                        current_search_area = current_search_area[idx+1:]
                        current_number += digit_char
                        break
            output += int(current_number)

    return output

if __name__ == "__main__":
    print(task1())
    print(task2())