"""
Binary Search
Time Complexity
best case : O(1)
average case : O(log n)
worst case : O(n)
"""

#-----Recursive-----
# def binarySearch(lst,item,left,right):
#     if(right>=left):
#         mid=(left+right)//2
#         if lst[mid]==item:
#             return (mid+1)
#         elif lst[mid]<item:
#             return binarySearch(lst,item,mid+1,right)
#         else:
#             return binarySearch(lst,item,left,mid-1)
#     else:
#         return -1
    
#-----Iterative-----
def binarySearch(lst,item,left,right):
    while right>=left:
        mid=(left+right)//2
        if lst[mid]==item:
            return (mid+1)
        elif lst[mid]<item:
            left=mid+1
        else:
            right=mid-1
    return -1

lst=list(map(int,input().split()))
item=int(input())
result=binarySearch(lst,item,0,len(lst))
if result==-1:
    print("item is not found")
else:
    print(f"item found at postion {result}")
    print(f"item found at index {result-1}")