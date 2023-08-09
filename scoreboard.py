FONT = ("Courier", 24, "normal")

from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Black")
    
    def increase(self):
        self.score += 1

    def display(self):
        self.penup()
        self.goto(-250, 250)
        self.write("LEVEL:" + str(self.score), font=("Courier", 24, "normal"))

