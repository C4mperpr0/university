
"""
fib = [0, 1]

while 1:
    try:
        x = int(input("Zahl: "))
        break
    except:
        print("Dit is keene Zahl mein Freundschen!")

while len(fib) < x:
    fib.append(fib[-2] + fib[-1])

print(fib[-1])

"""

while 1:
    try:
        x = int(input("Zahl: "))
        break
    except:
        print("Dit is keene Zahl mein Freundschen!")

def fib(n, x=0, y=1):
    if n > 0:
        return fib(n-1, y, x+y)
    else:
        return x

for i in range(x):
    print(fib(i))
