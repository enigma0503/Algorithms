
# END-SORT

"""Given a list  of N distinct integer numbers,
you can sort the list by moving an element to the end of the list.
Find the minimum number of moves required to sort the list
using this method in ascending order."""

#input 
arr=list(map(int,input().split(" ")))

#sort the given list
arr1 = sorted(arr)

count = 0
for i in range(len(arr)):
    if arr[i] == arr1[count]:
        count+=1
print(len(arr)-count)
