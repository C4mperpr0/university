from random import randrange as rr


x = {}
for i in range(10):
    x[rr(255)] = True
x = list(x.keys())


for i in range(len(x)):
    print(x)

    biggest = 256
    biggest_index = None

    for j in range(i, len(x)):
        if x[j] < biggest:
            biggest = x[j]
            biggest_index = j
    x[i], x[biggest_index] = (x[biggest_index], x[i])
print(x)
