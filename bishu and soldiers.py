n=int(input())
l=list(map(int,input().split()))
l.sort()

ans=[]
q=int(input())
for i in range(q):
        power=int(input())
        ans=[]
        s=0
        c=0
        for x in range(n):
            if l[x]<=power:
                c+=1
                s+=l[x]
                
            else:
                break
        
        ans.append(c)
        ans.append(s)
        print(" ".join(map(str,ans)))
          
                

            
    
