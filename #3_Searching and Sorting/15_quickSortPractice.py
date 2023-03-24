"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<pivot:
            i+=1
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
    i+=1
    temp=array[i]
    array[i]=pivot
    array[high]=temp
    return i
def quicksort(array,low,high):
    if low<high:
        pidx=partition(array,low,high)
        quicksort(array,low,pidx-1)
        quicksort(array,pidx+1,high)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test,0,len(test)-1)