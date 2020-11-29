from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_LIVES = 5
FONT = ("Courier", 24, "normal")

class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reposition()
        self.lives = STARTING_LIVES
        self.display_lives()


    def display_lives(self):
        self.lives_score = Turtle()
        self.lives_score.penup()
        self.lives_score.hideturtle()
        self.lives_score.goto(290, 250)
        hearts = []
        for _ in range(self.lives):
            hearts.append("💚")
        self.lives_score.write(f"{''.join(hearts)}", align="right", font=FONT)


    def move(self):
        self.forward(MOVE_DISTANCE)


    def reposition(self):
        self.goto(STARTING_POSITION)


    def lose_life(self):
        self.lives -= 1
        self.lives_score.clear()
        self.display_lives()


