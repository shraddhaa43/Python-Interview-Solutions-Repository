a = 0
b = 1
c = 0

for i in range(1, 6):
    for j in range(1, i + 1):
        if i == 1:
            print(c, end=" ")
            c = a + b
        else:
            print(c, end=" ")
            c = a + b
            a, b = b, c
    print()
