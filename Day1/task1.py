class Safe:
    def __init__ (self, initial_value=50):
        self.value = initial_value

    def is_valid(self):
        return 0 <= self.value <= 99

    def check(self):
        if self.value < 0:
            self.value = 100 + self.value
        if self.value > 99:
            self.value = self.value - 100

    def switch(self, direction, amount):
        if direction == "L":
            self.value -= amount
            while not self.is_valid():
                self.check()
        elif direction == "R":
            self.value += amount
            while not self.is_valid():
                self.check()

if __name__ == "__main__":

    code = 0
    safe = Safe()

    with open("input.data", "r") as input:
        for line in input:
            direction = line[0]
            amount = int(line[1:])
            safe.switch(direction, amount)
            if safe.value == 0:
                code += 1

    print(f"The code to open the safe is: {code}")