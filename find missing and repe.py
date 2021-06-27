arr=[2,3]
arr.sort()
l=[]
n=3
for i in range(0,n):
    if arr.count(arr[i])==2:
        l.append(arr[i])
        break
for i in range(1,n+1):
    if not (i  in  arr):
        l.append(i)
        break
print(l)
        
        
    
    
    
