def binary_search(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

#print(binary_search([5,4,8,9,6,4,6,5,10,11],6))
        
s="hari12"
print(s.isalnum())
print(any([char.isdigit() for char in s]))
            