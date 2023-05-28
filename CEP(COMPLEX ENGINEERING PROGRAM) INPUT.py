def CatsAndMouse(catA,catB,mouse):
    catA!=0
    catB!=0
    mouse=0
    if catA<catB:
        return(1)
    elif catA>catB:
        return(-1)
    elif catA==catB:
        return(0)
print("Consider mouse is at zero position")
x=int(input("Enter position of catA: "))
y=int(input("Enter position of catB: "))
z=0
if(x==0 and y==0 and z==0):
    print("Program ends")
else:
    CatsAndMouse(x,y,z)
    if CatsAndMouse(x,y,z)==1:
        print("catA")
    elif CatsAndMouse(x,y,z)==-1:
        print("catB")
    else:
        print("Mouse escape as two cats fought")
