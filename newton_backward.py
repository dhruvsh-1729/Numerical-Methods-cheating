f_init=1
x=0.0
h=0.1
steps=3
import math as m
lis=[f_init]

def fnew():
  f_new=(f_init+ h*(x**3)*(m.e)**-2*x)/(1+2*h)
  return f_new
  
print(fnew())

for i in range(0,steps):
  f=fnew()
  lis.append(f)
  f_init=lis[i+1]
  x+=h

print(lis)  
