f_init=1
x=0.0
h=0.1
steps=50
import math as m 
lis=[f_init]
def f_new():
  f_new=f_init+h*(-2*f_init + (x**3)*(m.e)**-2*x)
  return f_new
  
for i in range(0,steps):
  f=f_new()
  lis.append(f)
  f_init=lis[i+1]
  x+=h
  
print(lis)  
  
