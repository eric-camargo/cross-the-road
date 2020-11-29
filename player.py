from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")

class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reposition()


    def move(self):
        self.forward(MOVE_DISTANCE)


    def reposition(self):
        self.goto(STARTING_POSITION)




