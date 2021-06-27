def ismake(a,mid,p):
    time=0
    pt=0
    for i in range(len(a)):
        time=a[i]
        j=2
        while time<=mid:
            time+=a[i]*j
            pt+=1
            j+=1
            if pt>=p:
                return True
            
    return False
for _ in range(int(input())):
    p=int(input())
    a=list(map(int,input().split()))
    length=a[0]
    a.remove(a[0])

    low=0
    high=1000000007
    while low<=high:
        mid=(low+high)//2
        if (ismake(a,mid,p)):
            high=mid-1
            res=mid
        else:
            low=mid+1
    print(res)
    
