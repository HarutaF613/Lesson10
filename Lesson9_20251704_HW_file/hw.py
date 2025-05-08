import pgzrun
import random

HEIGHT = 800
WIDTH = 1200
TITLE = "Connect Point"

number_of_point = 15
points = []
lines = []
current_index = 0

def point_prodece():
    for i in range(number_of_point):
        point = Actor("point")
        point.x = random.randint(50,WIDTH-50)
        point.y = random.randint(50,HEIGHT-50)
        points.append(point)

def draw():
    screen.fill("Gray")
    number = 1
    for point in points:
        point.draw()
        screen.draw.text(str(number),(point.x+10,point.y+10),fontsize = 30, color="Black")
        number += 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255),)

def update():
    pass

def on_mouse_down(pos):
    global lines,current_index
    print("Debug1")
    print(current_index)
    print(number_of_point)
    print(points[current_index].pos)
    if current_index < number_of_point:
        if points[current_index].collidepoint(pos):
            print(points[current_index])
            if current_index:
                print("Debug")
                lines.append((points[current_index-1].pos,points[current_index].pos))
                print(lines)
        current_index += 1
    else:
        lines= []
        current_index = 0

point_prodece()
pgzrun.go()