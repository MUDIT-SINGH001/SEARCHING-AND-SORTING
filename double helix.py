def DoubleHelix(A,B,m,n):
  sum1 = 0
  sum2 = 0
  i = 0
  j = 0
  while i < m and j < n:
    if A[i] < B[j]:
      sum1 += A[i]
      i+=1
    elif A[i] > B[j]:
      sum2 += B[j]
      j+=1
    else:
      sum1 += A[i]
      sum2 += B[j]
      sum1 = sum2 = max(sum1, sum2)
      i=i+1
      j=j+1
  while i < m:
    sum1 += A[i]
    i+=1
  while j < n:
    sum2 += B[j]
    j+=1
  return max(sum1, sum2)


for _ in range(int(input())):
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    m,n=len(a1),len(a2)
    print(DoubleHelix(a1,a2,m,n))
   
  
