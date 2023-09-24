#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def pair(arr,sum1):
    pairs=[]
    seen={}
    for num in arr:
        complement =sum1-num
        if complement in seen:
            pairs.append((complement,num))
        seen[num]=True
    return pairs
arr = [1,2,3,4,5,6]
sum1=7
result=pair(arr,sum1)
print(result)
