# Write a program which, given the length of three sides of a triangle, will determine whether the triangle is right- angled. Assume
# that the third argument to the function is always the longest side. It will return True if the triangle is right-angled,
# or False otherwise.

sideA = input("Please enter the side A!")
sideB = input("Please enter the side B!")
sideC = input("Please enter the side C!")

sideA = float(sideA)
sideB = float(sideB)
sideC = float(sideC)

if sideC > sideA and sideC > sideB:
    print("True")
else:
    print("False")
