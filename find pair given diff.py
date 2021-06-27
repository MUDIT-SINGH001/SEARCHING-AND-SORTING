n=265
arr=list(map(int,input().split()))
f=0
for i in range(len(arr)):
    if (arr[i]+n) in arr:
        f=1
        break
if f==1:
    print(1)
else:
    print(-1)
