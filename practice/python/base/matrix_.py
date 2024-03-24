a = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, -1] #-1 # len(a) - 1
]

n = 3
# matrix_ = [[int(i) for i in input().split()] for i in range(n)]

for i in a:
    for j in i:
        print(j, end = " ")
    print()

