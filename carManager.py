COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import Turtle, Screen
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.penup()
        self.goto(280, random.randint(-240, 260))
        self.movement = 1
    
    def Move(self):
        x = self.xcor() - self.movement
        y = self.ycor()
        self.goto(x, y)
        
    
    def Remove(self):
        if(self.xcor() < -250):
            self.clear()
    

