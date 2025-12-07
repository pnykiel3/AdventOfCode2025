import sys


def task1():
    try:
        with open("input.data", "r") as infile:
            lines = [line.rstrip('\n') for line in infile]
    except FileNotFoundError:
        sys.stderr.write("Failed to open input.data\n")
        sys.exit(-1)

    if not lines:
        sys.stderr.write("input.data is empty\n")
        sys.exit(-1)

    y = len(lines)
    x = len(lines[0])

    arr = [['.'] * y for _ in range(x)]
    start = (0, 0)

    for ys in range(y):
        line = lines[ys]
        # Processing line {ys}: {line}
        for xs in range(x):
            if line[xs] == 'S':
                arr[xs][ys] = 'S'
                start = (xs, ys)
            elif line[xs] == '^':
                arr[xs][ys] = '^'
            
                
    #print(f"Created array {x}x{y}")
    counter = 0

    for yid in range(1, y):
        for xid in range(x):
            
            if arr[xid][yid-1] == 'S':
                arr[xid][yid] = '|'
            elif arr[xid][yid] == '.' and arr[xid][yid-1] == '|':
                arr[xid][yid] = '|'
            elif arr[xid][yid] == '^' and arr[xid][yid-1] == '|':
                    arr[xid-1][yid] = '|'
                    arr[xid+1][yid+1] = '|'
                    counter += 1

    
    
    return counter


    

if __name__ == "__main__":
    result1 = task1()
    print(f"Result 1: {result1}")


