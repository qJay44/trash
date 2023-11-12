from turtle import *

shape('turtle')
speed(0)


def snowFlake_sides(lenghth, levels):
    if levels == 0:
        forward(lenghth)
        return
    
    lenghth /= 3.0
    snowFlake_sides(lenghth, levels - 1)
    left(60)
    snowFlake_sides(lenghth, levels - 1)
    right(120)
    snowFlake_sides(lenghth, levels - 1)
    left(60)
    snowFlake_sides(lenghth, levels - 1)

def snowFlake(sides, length):
    for _ in range(sides):
        snowFlake_sides(length, sides)
        right(360 / sides)


# def tree(size, levels, angle):
#     if levels == 0: 
#         color('green')
#         dot(size)
#         color('brown')
#         return
#     forward(size)
#     right(angle)

#     tree(size * 0.8, levels - 1, angle)
#     left(angle * 2)

#     tree(size * 0.8, levels - 1, angle)
#     right(angle)

#     backward(size)

# left(90)
# tree(70, 5, 30)
snowFlake(3, 400)
mainloop()