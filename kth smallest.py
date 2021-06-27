for _ in range(int(input())):
        N,Q=map(int,input().split())
        l=[]
        for i in range(N):
            l.append(list(map(int,input().split())))
            
        l.sort()
        #print(l)
        temp=[l[0]]
        
        
        j=0
        for i in range(1,N):
            
           if temp[j][1]>=l[i][0] and temp[j][1]<l[i][1]:
               temp[j][1]=l[i][1]
               

           elif temp[j][1]<l[i][0]:
               temp.append(l[i])
               j+=1
    #print(temp)
        d={}
        r=0
        for i in range(len(temp)):
            r+=temp[i][1]-temp[i][0]+1
            d[temp[i][1]]=r
     
        for  i in range(Q):
            query=int(input())
            f=0
            for key , val in d.items():
                if query <=val:
                    lim=val-query
                    print(key-lim)
                    f=1
                    break
            if f==0:
                print(-1)
