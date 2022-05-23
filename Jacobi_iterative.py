
#To find solution of a three variable system using Jacobi iteration method

co=[[20,1,-2,17],[3,20,-1,-18],[2,-3,20,25]]
ans=[]
x1=x2=x3=0
steps=5
for i in range(steps):
  lis=[]
  x1_new=(co[0][3]-(x2*co[0][1]+x3*co[0][2]))/co[0][0]
  x2_new=(co[1][3]-(x1*co[1][0]+x3*co[1][2]))/co[1][1]
  x3_new=(co[2][3]-(x1*co[2][0]+x2*co[2][1]))/co[2][2]
  lis.append(x1_new)
  lis.append(x2_new)
  lis.append(x3_new)
  ans.append(lis)
  x1=x1_new
  x2=x2_new
  x3=x3_new

print(ans)
