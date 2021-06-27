def iscut(a,m,mid):
    sums=0
    for i in range(len(a)):
        if mid<a[i]:
            sums+=a[i]-mid
            if sums>=m:
                return True
    
    return False
            


for _ in range(int(input())):
        n,m=map(int,input().split())
        a=list(map(int,input().split()))
        low=0
        high=sum(a)
        res=-1
        while(low<=high):
            mid=(low+high)//2
            if (iscut(a,m,mid)):
                low=mid+1
                res=mid
            else:
                high=mid-1
        print(res)
