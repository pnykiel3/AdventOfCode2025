if __name__ == "__main__":

    output = 0

    with open("input.data", "r") as input:

        data = input.read().split(',')
        for line in data:
            min = line.split('-')[0]
            max = line.split('-')[1]

            for i in range(int(min), int(max) + 1):
                number = str(i)
                if (len(number) % 2) == 0:
                    firstpart, secondpart = number[:len(number)//2], number[len(number)//2:]
                    if firstpart == secondpart:
                        output += i

    print(f"The valid password is: {output}")