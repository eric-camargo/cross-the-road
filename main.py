import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("GhostWhite")
car_manager = CarManager()

screen.listen()
screen.onkey(car_manager.speed_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.is_lane_free()
    car_manager.move_cars()
    car_manager.make_cars()
