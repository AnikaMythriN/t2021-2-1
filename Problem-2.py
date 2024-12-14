def series(n):
   a=[]
   for i in range(n):
         a.append(1+2*i)
   return ",".join(map(str,a))

n=int(input("Enter the number :"))
res=series(n)
print(f"The result is : {res}")