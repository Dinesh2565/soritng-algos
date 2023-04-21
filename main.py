

                #binary search algorithm
"""
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1




arr=[1,2,4,5,8,9,15,18,19]
target=19



pointer=binary_search(arr, target)

if pointer!=-1:
    print('the number you have entered is the in position: ' + str(pointer))
else:
    print('the value you have entered is not in the array') */

"""




    #selection sort algorithm
'''

def sel_sort(arr):
    for i in range(len(arr)):
        min_index=i  # to track the least value and its index
        for j in range(i,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j      #swapping the values of the current least number in the array 

        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[10,15,5,2,3,0,14,8]
result=sel_sort(arr)
print(result)
            
'''



#Bubble sort algo

arr=[10,15,5,2,3,0,14,8]
'''
def Bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(Bubble(arr))
'''

#insertion sort
'''
def insertion(arr):
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(insertion(arr))
'''


# merge sort

def merge(arr):
    f