#2: Write a program which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse
import math
sideA=input("Please enter the side A!")
sideB=input("Please enter the side B!")

sideA=float(sideA)
sideB=float(sideB)

sideC=(sideA**2)+(sideB**2)
sideC=math.sqrt(sideC)
print("The length of your Hypotnuse is ", sideC)