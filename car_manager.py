import random
from player import FINISH_LINE_Y, STARTING_POSITION
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ROAD = FINISH_LINE_Y - STARTING_POSITION[1]
LANE_HEIGHT = 20
LANES_DISTANCE = 10
LANE_START_X = 300
NEW_CARS_RATE = (0, 5)
NEW_CAR_CHANCES = 0.2


class CarManager():

    def __init__(self):
        self.lanes = []
        self.make_lanes()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.make_cars()


    def make_lanes(self):
        print(ROAD)
        lanes_num = (ROAD - 10) // (LANE_HEIGHT + LANES_DISTANCE)
        print(lanes_num)
        starting_y = STARTING_POSITION[1] + LANES_DISTANCE + LANE_HEIGHT/2
        for lane in range(lanes_num):
            lane_y = starting_y + lane * (LANE_HEIGHT + LANES_DISTANCE)
            self.lanes.append(lane_y)


    def make_cars(self):
        if random.random() < NEW_CAR_CHANCES:
            self.cars.append(Car(self.lanes))


    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)


    def speed_up(self):
        self.speed += MOVE_INCREMENT
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
        self.color = random.choice(COLORS)
