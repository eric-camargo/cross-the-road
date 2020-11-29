from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_LIVES = 5

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.display_score()
        self.lives = STARTING_LIVES
        self.display_lives()

    def update_display(self):
        self.clear()
        self.display_score()
        self.display_lives()

    def display_score(self):
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)


    def level_up(self):
        print("Level up!")
        self.score += 1
        self.update_display()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


    def display_lives(self):
        self.goto(280,250)
        hearts = []
        for _ in range(self.lives):
            hearts.append("💚")
        self.write(f"{''.join(hearts)}", align="right", font=FONT)

    def lose_life(self):
        self.lives -= 1
        self.update_display()
