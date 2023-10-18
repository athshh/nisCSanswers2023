import math

print("Enter coefficients of the terms in the equation [ax^2+bx+c=0]")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D = (b**2)-4*a*c

if a==0:
    print("Quadratic Equation cannot have coefficient of x^2 value as zero.")
else:
    if D<0:
        print("The roots are imaginary and infinite.")
    elif D==0:
        root=((-1*b)+(math.sqrt(D)))/2*a
        print("Roots are real and same")
        print("Root 1 =",root,"and root 2 =",root)
    else:
        root1=((-1*b)+(math.sqrt(D)))/2*a
        root2=((-1*b)-(math.sqrt(D)))/2*a
        print("Roots are real and distinct")
        print("Root 1 =",root1,"and root 2 =",root2)