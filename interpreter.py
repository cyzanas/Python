x,y,z=input("Expression:").split()
x=int(x)
z=int(z)
if y=="+":
    sum=x+z
    sum=float(sum)
    print(sum)
elif y=="-":
    sum=x-z
    sum=float(sum)
    print(sum)
elif y=="*":
    sum=x*z
    sum=float(sum)
    print(sum)
elif y=="/":
    sum=x/z
    sum=float(sum)
    print(sum)


else:
    print("what is this")
