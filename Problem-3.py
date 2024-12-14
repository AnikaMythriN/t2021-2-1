def series(a):
   x= a if a % 2 != 0 else a-1
   res=[]
   n=1
   if a==1 or a==2:
       res=[1] 
   else:
       while len(res)<x and n<=2*x-1:
           res.append(n)
           n+=2
   return res

a=int(input("Enter the number :"))
s=series(a)
print(f"The result is : ")
print(", ".join(map(str,s)))



