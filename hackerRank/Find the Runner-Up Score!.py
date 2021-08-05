# arr = map(int, input("arr").split())
# print(list(arr))
arr=[2, 3, 6, 6, 5]
n=5
"""
c=[]
result=0
print(len(arr))
for i in range(len(arr)):
    if arr[i]==arr[i+1]:
        c.extend(arr[i:i+2])
        for m in c:
            arr.remove(m)
    elif result<arr[i]:
        result=arr[i] 

print(result)
"""

m1 = max(arr)
m2 = -9999999999
for i in range(n):
    if arr[i] != m1 and arr[i] > m2:
        m2 = arr[i]
        print (m2)
    

    
        