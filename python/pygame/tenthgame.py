

def sort(arr) :
    for i in range(1, len(arr)) :
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0 :
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

arr = [10-i for i in range(0, 10)]

print(arr)
sort(arr)
print(arr)