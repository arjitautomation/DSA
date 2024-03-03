# Insertion sort in Python

def insert(arr):
    for i in range(1,len(arr)):
        j=i
        while (arr[j-1] > arr[j] and j>0):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1

arr=[7,8,2,9]
insert(arr)
print(arr)