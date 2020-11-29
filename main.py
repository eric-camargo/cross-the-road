import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("GhostWhite")
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(car_manager.speed_up, "q")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.is_lane_free()
    car_manager.move_cars()
    car_manager.make_cars()

    if player.ycor() >= FINISH_LINE_Y:
        player.reposition()
        car_manager.speed_up()
        scoreboard.level_up()
    dead = 0
    for car in car_manager.cars:
        if car.distance(player) < 20:
            player.reposition()
            scoreboard.lose_life()
            if scoreboard.lives <= 0:
                game_is_on = False

screen.exitonclick()