from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)


    def level_up(self):
        print("Level up!")
        self.score += 1
        self.update_display()
