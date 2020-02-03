# 8: Write a program that counts the number of even digits in the scope of 1—1000.
evenCount = 0
for number in range(1, 1001):
    if (number % 2) == 0:
        print("The number ", number, "is even!")
        evenCount = evenCount+1
print("The count of even numbers is ", evenCount, "!")


