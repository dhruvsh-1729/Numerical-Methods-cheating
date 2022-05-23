
import math as m 
x=0.0
limit1=0
limit2=1
steps=10
sum=0
h=(limit2-limit1)/steps

lis=[]

for i in range(0,steps):
  lis.append(m.sqrt(1-x**2))
  x+=h
  
for j in range(0,steps):
  if j==0 or j==steps-1:
    sum+=lis[j]
  elif j%2==0:
    sum+=2*lis[j]
  else:
    sum+=4*lis[j]
    
print((h/3)*sum) 
