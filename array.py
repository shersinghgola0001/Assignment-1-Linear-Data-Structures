#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def rev_arr(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
arr=[1,2,3,4,5]
rev_arr(arr)
print(arr)  
