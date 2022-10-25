primes = [2]

while 1:
    try:
        x = int(input("Zahl: "))
        break
    except:
        print("Dit is keene Zahl mein Freundschen!")

for i in range(3, x+1):
    if str(i)[-4:] == "0000":
        print(i)
    is_prim = True
    for p in primes:
        if i % p == 0:
            is_prim = False
    if is_prim:
        primes.append(i)

if primes[-1] == x:
    print(f"{x} is wohl ne primzahl")
else:
    print(f"{x} is leider keene prime wa")
