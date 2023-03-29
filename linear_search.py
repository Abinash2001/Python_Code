"""
Linear Search
time complexity
best case : O(1)
wrost case : O(n)
"""

def linearSearch(lst,item):
    for i in range(len(lst)):
        if lst[i]==item:
            print(f"item found in index : {i}")
            print(f"item found in position : {i+1}")
            return
    print("item not found")

lst=list(map(int,input().split()))
item=int(input())
linearSearch(lst,item)