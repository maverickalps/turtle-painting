import turtle as turtle_module
import random
turtle_module.colormode(255)

tim = turtle_module.Turtle()


rgb = [
    (177, 6, 35), (13, 102, 155), (9, 64, 37), (248, 239, 243),
    (229, 47, 10), (237, 246, 239), (173, 173, 24), (66, 40, 7), (114, 62, 93),
    (6, 22, 73), (13, 128, 14), (159, 190, 185), (60, 36, 125), (206, 4, 2),
    (231, 240, 247), (8, 85, 35), (30, 9, 16), (249, 217, 2), (31, 149, 215),
    (214, 54, 58), (219, 53, 48), (192, 164, 140), (234, 215, 65), (143, 176, 191),
    (194, 142, 154), (234, 171, 161), (230, 168, 178), (15, 79, 106), (88, 64, 26)
]
def move(no_of_dots):
    for _ in range (no_of_dots):
        tim.dot(12,random.choice(rgb))
        tim.forward(22)
tim.penup()
# tim.speed(0)
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)

def dots(n):
    for _ in range(n):
        move(30)
        tim.left(90)
        tim.forward(20)
        tim.left(90)
        tim.forward(660)
        tim.setheading(0)

# dots(10)




# made second update for higher concentration of dots on the screen.
tim.speed(10)
tim.setheading(220)
tim.forward(420)
tim.setheading(0)
dots(30)

screen = turtle_module.Screen()
screen.exitonclick()
