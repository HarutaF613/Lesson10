import os
x = 0
y = 25
os.environ["SDL_VIDEO_WINDOW_POS"] = f"{x},{y}"

import pgzrun
import random

WIDTH = 1440
HEIGHT = 960
TITLE = "Happy Mothers Day"

def animation():


def draw():
    screen.fill("White")
    animation()
    screen.draw.text("Happy Mothers Day",center = (WIDTH/2,100),fontsize = 100, color="Red", shadow = (1,1),scolor = "Gray")
def update():
    pass 

pgzrun.go()