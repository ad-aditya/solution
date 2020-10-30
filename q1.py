def tri(side1,side2,side3):
	perim =side1+side2+side3
	s=perim/2
	area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
	inf=list()
	inf.append(perim)
	inf.append(area)
	tup=tuple(inf)
	return tup
sides=list()
side1=float(input("enter first side of triangle"))
side2=float(input("enter second side of triangle"))
side3=float(input("enter third side of triangle"))
if(side1+side2<side3):
	print("invalid sides")
elif(side2+side3<side1):
	print("invalid sides")	
elif(side3+side1<side2):
	print("invalid sides")
else:
     sides.append(side1)
     sides.append(side2)
     sides.append(side3)
     print("the perimeter and area of triangle are" ,tri(sides[0],sides[1],sides[2]) )
