
for _ in range(int(input())):
    N,C=map(int,input().split())
    a=[]
    for i in range(N):
        a.append(int(input()))
    a.sort()
    low=1
   
    high=a[N-1]
    

    while low<high:
        mid=(low+high)//2
        c=1
        ini=a[0]
        for i in range(1,N):
            if a[i]-ini>=mid:
                c+=1
                ini=a[i]
        if c>=C:
                    low=mid+1
                    res=mid

        else:
                    high=mid-1
            
    print(res)    
        
    
                
        
