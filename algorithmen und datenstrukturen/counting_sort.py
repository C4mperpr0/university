from random import randrange as rr

arr = []
for i in range(20):
    arr.append(rr(10))

def countingSort(arr):
    r = [0] * (max(arr) + 1) # +1 to include 0

    for num in arr:
        r[num] += 1

    r_arr = []
    for num in range(max(arr) + 1):
        for i in range(r[num]):
            r_arr.append(num)

    return r_arr

print(f"unsorted: {arr}")
sorted_arr = countingSort(arr)
print(f"counting sort: {sorted_arr}")
print(f"pythons tim-sort: {sorted(arr)}")
print(f"Ist das gleiche: {'positiv' if sorted_arr == sorted(arr) else 'nö'}")
