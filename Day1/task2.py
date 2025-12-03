if __name__ == "__main__":
cd ..
    code = 0
    value = 50

    with open("input.data", "r") as input:
        for line in input:
            direction = line[0]
            amount = int(line[1:])

            if direction == "L":
                for _ in range(amount):
                    value = (value - 1) % 100
                    if value == 0:
                        code += 1
            elif direction == "R":
                for _ in range(amount):
                    value = (value + 1) % 100
                    if value == 0:
                        code += 1

    print(f"The code to open the safe is: {code}")