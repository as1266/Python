# 6: Use for loops to make a turtle draw these regular polygons(regular means all sides the same lengths, all angles the same):
#  An equilateral triangle  • A hexagon (six sides)
import turtle

window = turtle.Screen()
window.title("Turtle Shapes!")

hex =turtle.Turtle()
hex.up()
hex.forward(-70)
hex.down()
for i in range (6):
    hex.forward(30)
    hex.left(60)

triangle = turtle.Turtle()
for i in range (3):
    triangle.forward(50)
    triangle.left(120)
window.mainloop()
