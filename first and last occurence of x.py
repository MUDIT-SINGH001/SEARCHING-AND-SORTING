arr=[1,3,5,5,5,5,67,123,125]
l=[ind for ind,val in enumerate(arr) if val==5]
print(min(l),max(l))
