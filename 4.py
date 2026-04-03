import math
# program to find roots of quadratic equation

a=float(input("Enter coefficient a:"))
b=float(input("Enter coefficient b:"))
c=float(input("Enter coefficient c:"))
d=b**2-4*a*c

if d>0:
   root1=(-b+math.sqrt(d))/(2*a)
   root2=(-b-math.sqrt(d))/(2*a)
   print(f"root1={root1} and root2={root2}")
elif d==0:
    root=-b/(2*a)
    print(f"root={root}")
else:
    print("Roots are imaginary")