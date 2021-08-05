arr=[1,2,2,3,4,5]
#arr.remove(1,3) #it accept only one argument arr.remove(1) 
#new=arr.remove(1) it can be assigned to another variable
"""
return item that have been removed
new=arr.pop(0)
print(new)

"""
"""
print(len(arr))
for i in range (len(arr)-1):
    if arr[i] == arr[i+1]:
        print("print hello")
"""



"""
arr.sort(reverse=True)
print(arr)
without assign to another variable
"""
# arr1 = list(map(int, input("input ").split()))
# print(arr1)
"""
iff you do it with for i in iterable don t gave you index it give item
arr1=[1, 2, 3, 4, 5]
for i in range(len(arr1)):
    if i < len(arr1)-1:
         print(arr1[i+1])
"""
"""
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(arr[i])
        
        
"""
"""
bls=[1,1,2]
al=bls.copy()

for i in range(len(bls)-1):
    if bls[i]==bls[i+1]:
        al.pop(i)
        print(bls)
        al.pop(i)
        print(bls)
"""
bls=[1,1,2]
n=bls.count(1)
print(n)