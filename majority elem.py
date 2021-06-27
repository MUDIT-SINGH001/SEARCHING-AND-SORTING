a=[3,1,2]
N=3
m=N//2
elem=0
for i in range(0,N):
    if a.count(a[i])>m:
        m=a.count(a[i])
        elem=a[i]
if elem:
    print(elem)
else:
    print(-1)
    
