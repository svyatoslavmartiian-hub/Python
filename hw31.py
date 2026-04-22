# 1
import random
import turtle

# turtle.pencolor("red")
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

# turtle.penup()
# turtle.forward(150)
# turtle.pendown()

# turtle.pencolor("green")
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)

# turtle.penup()
# turtle.forward(150)
# turtle.pendown()

# turtle.pencolor("blue")
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)

# turtle.done()

#  2

# turtle.speed(3)

# turtle.pencolor("black") 
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)


# turtle.pencolor("black") 
# turtle.fillcolor("orange") 
# turtle.begin_fill() 


# for _ in range(3):
#     turtle.forward(100)
#     turtle.left(120)

# turtle.end_fill() 


# turtle.hideturtle()


# turtle.done()



# 3

turtle.speed(0) 
turtle.colormode(255) 

for i in range(36):
    
    c_1 = random.randint(0, 255)
    c_2 = random.randint(0, 255)
    c_3 = random.randint(0, 255)
    turtle.pencolor(c_1, c_2, c_3)
    
    for side in range(4):
        turtle.forward(100)
        turtle.left(90)
    
    turtle.left(10)

turtle.done()