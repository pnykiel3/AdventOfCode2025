if __name__ == "__main__":

    output = 0

    with open("input.data", "r") as input:

        data = input.read().split(',')
        for line in data:
            min = line.split('-')[0]
            max = line.split('-')[1]

            for i in range(int(min), int(max) + 1):
                number = str(i)
                n_len = len(number)
                valid = False

                for pattern in range (1, n_len // 2 +1) :
                    if n_len % pattern == 0:
                        firstpart = number[:pattern]
                        multiples = n_len // pattern
                        if firstpart * multiples == number:
                            valid = True
                            break
                if valid:
                    output += i

    print(f"The valid password is: {output}")

