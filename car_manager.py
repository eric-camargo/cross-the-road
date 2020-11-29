import random
from player import FINISH_LINE_Y, STARTING_POSITION
from turtle import Turtle
import numpy as np

COLORS = ["gold1", "red3", "SpringGreen1", "VioletRed", "OliveDrab1", "aquamarine", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ROAD = FINISH_LINE_Y - STARTING_POSITION[1]
LANE_HEIGHT = 20
LANES_DISTANCE = 10
LANE_START_X = 300
FREE_LANE_X = 260
NEW_CARS_RATE = (0, 5)
NEW_CAR_CHANCES = 0.10


class CarManager():

    def __init__(self):
        self.lanes = []
        self.make_lanes()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.new_car_rate = NEW_CAR_CHANCES
        self.make_cars()

    def make_lanes(self):
        print(ROAD)
        lanes_num = (ROAD - 10) // (LANE_HEIGHT + LANES_DISTANCE)
        print(lanes_num)
        starting_y = STARTING_POSITION[1] + LANES_DISTANCE + LANE_HEIGHT/2 + 10
        for lane in range(lanes_num):
            lane_y = starting_y + lane * (LANE_HEIGHT + LANES_DISTANCE)
            self.lanes.append(lane_y)


    def is_lane_free(self):
        self.busy_lanes = []
        for car in self.cars:
            if car.xcor() > FREE_LANE_X:
                self.busy_lanes.append(car.ycor())


    def make_cars(self):
        for car in self.cars:
            if car.xcor() < -400:
                self.cars.remove(car)
        self.is_lane_free()
        if random.random() < self.new_car_rate:
            free_lanes = np.setdiff1d(self.lanes, self.busy_lanes)
            self.cars.append(Car(free_lanes))


    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)


    def speed_up(self):
        increase_rate = MOVE_INCREMENT/self.speed
        self.speed += MOVE_INCREMENT
        self.new_car_rate *= (1 + increase_rate)
        print(self.speed)

class Car(Turtle):

    def __init__(self, lanes):
        super(Car, self).__init__()
        self.lanes = lanes
        self.new_car()
        self.position_car()


    def position_car(self):
        self.lane = random.choice(self.lanes)
        self.goto(LANE_START_X, self.lane)


    def move(self, speed):
        new_x = self.xcor() - speed
        self.setx(new_x)


    def new_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
