
def recursive_faculty(n, x=0):
    if x == 0:
        return recursive_faculty(n-1, n)
    if n >= 1:
        return recursive_faculty(n-1, x*n)
    else:
        return x

#print(recursive_faculty(int(input("Number:"))))

from threading import Thread

t1 = Thead(target=recursive_faculty, args=(1))
t1.start()
