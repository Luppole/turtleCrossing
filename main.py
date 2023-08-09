import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.Move)

game_is_on = True
carList = []
counter = 0
car = CarManager()

while game_is_on:
    time.sleep(0.1)
    if(counter == 7):
        car = CarManager()
        counter = 0
    else:
        counter += 1

    carList.append(car)    
    for cars in carList:
        player.Collision(cars)
        car.movement *= (scoreboard.score+1)**2
        cars.Remove()
        cars.Move()
    
    if(player.Finish()):
        scoreboard.increase()
        print(scoreboard.score)
        scoreboard.clear()

    if(player.Collision(car)):
        scoreboard.score = 0
    
    scoreboard.display()
    screen.update()

