euler=[]

max_euler=1000

i=1
while i*3<max_euler:
  euler.append(i*3)
  i+=1

i=1
while i*5<max_euler:
  if i*5 not in euler:
    euler.append(i*5)
  i+=1

euler.sort()
print(euler)

sum=0
for i in euler:
  sum+=i
print(sum)