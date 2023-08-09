STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
    
    def Move(self):
        x = self.xcor()
        y = self.ycor() + MOVE_DISTANCE
        self.goto(x, y)

    def Collision(self, car):
            if(self.distance(car) <= 30):
                self.goto(STARTING_POSITION)
                return True
            
    
    def Finish(self):
        if(self.ycor() >= FINISH_LINE_Y):
            self.goto(0, -280)
            return True
            

    
