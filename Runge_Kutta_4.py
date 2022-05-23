import math as m 
f_init=1
x=0.0
h=0.1
semi=h/2
steps=3
 
def f(x,y):
  func=-2*y+(x**3)*(m.e)**-2*x
  return func
lis=[f_init]  
for i in range(0,steps):
  k1=f(x,f_init)
  k2=f(x+semi,f_init+semi*k1)
  k3=f(x+semi,f_init+semi*k2)
  k4=f(x+h,f_init+h*k3)

  fnew=f_init+(h/6)*(k1+2*k2+2*k3+k4)
  
  lis.append(fnew)
  f_init=fnew
  x+=h
  
print(lis)  
