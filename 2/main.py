import turtle


def snowflake(length, levels):
    if levels == 0:
        turtle.forward(length)
        return
    length /= 3.0
    snowflake(length, levels - 1)
    turtle.left(60)
    snowflake(length, levels - 1)
    turtle.right(120)
    snowflake(length, levels - 1)
    turtle.left(60)
    snowflake(length, levels - 1)


turtle.shape('turtle')
turtle.speed(9999)
length = 300.0
turtle.penup()
turtle.backward(length / 2.0)
turtle.pendown()
for i in range(3):
    snowflake(length, 4)
    turtle.right(120)

turtle.mainloop()
