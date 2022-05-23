
x_init=0.75

ans=[]
steps=10

for i in range(steps):
  result=(1+x_init)**-0.5
  ans.append(result)
  x_init=result
  
print(ans)  
