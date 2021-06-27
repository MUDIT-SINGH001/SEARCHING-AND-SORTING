def isallocated(a,mid,M):
    sums=0
    count=1
    for  i in  range(len(a)):
            if a[i]>mid:
                return False
            
            if  (sums+a[i]>mid):
                count+=1
                sums=a[i]
                if count>M:
                    return False
            else:
                sums+=a[i]
 
    return  True
    

a=[51,151,227,163,55]

M=3
low=0
high=sum(a)
res=-1
while low<=high:
    mid=(low+high)//2
    
    if  (isallocated(a,mid,M)):
        res=mid
        high=mid-1
        
        print(res)
    else:
        low=mid+1
print(res)  
