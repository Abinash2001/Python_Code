def binarySearch(lst,item,left,right):
    if(right>=left):
        mid=(left+right)//2
        if lst[mid]==item:
            return (mid+1)
        elif lst[mid]<item:
            return binarySearch(lst,item,mid+1,right)
        else:
            return binarySearch(lst,item,left,mid-1)
    else:
        return -1

lst=list(map(int,input().split()))
item=int(input())
result=binarySearch(lst,item,0,len(lst))
if result==-1:
    print("item is not found")
else:
    print(f"item found at postion {result}")
    print(f"item found at index {result-1}")