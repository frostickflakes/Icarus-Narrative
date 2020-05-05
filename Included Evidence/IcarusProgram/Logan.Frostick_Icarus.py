from vpython import *
#GlowScript 2.9 VPython
from visual import *

scene.caption = """
- Rotate "camera", drag with right button or Ctrl-drag.
- Zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
- Pan left/right and up/down, Shift-drag. """

"""Light Effects from the Sun"""
[distant_light(direction=vector( 0.22,  0.44,  0.88),       color=color.gray(0.8)), #Darker Gray
 distant_light(direction=vector(-0.88, -0.22, -0.44),       color=color.gray(0.3))] #Brighter Gray
distant_light(direction=vector(0,0,0), color=color.red) #Red with no shading

"""Additional light effects from a lamp"""
lamp = local_light(pos=vector(0,0,0), #Light Effects in the Center
                      color=color.yellow) #Yellow

"""Text for my Name above"""
text(text='Logan Frostick', #Name
    pos=vector (-4.35, +4.9, 4.65), depth=-0.45, #Sizing
    color=color.grey) #Regular Grey

"""
vector(x, y, z) 
x: width
y: height
z: depth
"""

"""Box Value"""
side = 4.5 
thick = 0.25
height = 2*side - thick
width = 2*side + thick

"""Top w/ Name Value"""
TSide = side*1.18
THeight = 4.4
TThick = thick*5.72
TWidth = width-8.8

"""Ground Value"""
GSide = -side-.25
GWidth = width*2
ZWidth = width*1.5

"""
Wall with "see through" front
Ri: Right
Le: Left
Bu: Buttom
To: Top
BK: Back
"""

wallRi = box (pos=vector(side, 0, 0), size=vector(thick, height, width),  color = color.purple) #Right
wallLe = box (pos=vector(-side, 0, 0), size=vector(thick, height, width),  color = color.purple) #Left
wallBu = box (pos=vector(0, -side, 0), size=vector(width, thick, width),  color = color.magenta) #Buttom
wallTo = box (pos=vector(0,  side, 0), size=vector(width, thick, width),  color = color.magenta) #Top
wallBK = box(pos=vector(0, 0, -side), size=vector(height, height, thick), color = color.magenta) #Back
Title = box (pos=vector(0,  TSide, THeight), size=vector(width, TThick, TWidth),  color = color.purple) #Top
Ground = box (pos=vector(0, GSide, 0), size=vector(GWidth, thick, ZWidth), color = color.magenta, texture=textures.stucco) #Buttom

"""
Ball, Trail, Mass, Velocity, Arrow
Retain - Trail Distance
"""

ball = sphere(pos=vector(-0.2,-0.1,+0.5),color=color.white, radius=0.33, make_trail=True, retain=40.0)  #Size, Color, Trail, Trail Distance
ball.mass = 1.0                                                                                 #Mass
ball.velocity = vector (+0.16, -0.24, -0.32)                                                    #Speed in Each Direction
vscale = 0.2                                                                                    #Multiplier
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, shaftwidth = 0.185, color=color.cyan)     #Arrow

ball2 = sphere (pos=vector(0.5,-0.6,-0.2),color = color.cyan, radius = 0.33, make_trail=True, retain=40)
ball2.mass = 1.0
ball2.velocity = vector (+0.24, +0.22, +0.30)
vscale2 = 0.2                                                                                    #Multiplier
varr2 = arrow(pos=ball2.pos, axis=vscale2*ball2.velocity, shaftwidth = 0.185, color=color.gray(0.7))     #Arrow

ball3 = sphere (pos=vector(0.5,-0.7,0),color = color.yellow, radius = 0.33, make_trail=True, retain=40)
ball3.mass = 1.0
ball3.velocity = vector (-0.25, +0.18, -0.22)
vscale3 = 0.2                                                                                    #Multiplier
varr3 = arrow(pos=ball2.pos, axis=vscale2*ball2.velocity, shaftwidth = 0.185, color=color.red)     #Arrow

ball4 = sphere (pos=vector(0.2,0.7,-0.4),color = color.red, radius = 0.33, make_trail=True, retain=40)
ball4.mass = 1.0
ball4.velocity = vector (+0.22, -0.24, +0.28)
vscale4 = 0.2                                                                                    #Multiplier
varr4 = arrow(pos=ball2.pos, axis=vscale2*ball2.velocity, shaftwidth = 0.185, color=color.yellow)     #Arrow

"""
- Where the Ball Contacts the Wall
- dt = Date Time (Speed)
- Direction of the Arrow
"""


side = side - thick*1.4 - ball.radius

"""While True Statement"""
dt = 0.15 #Multiplier
while True:
    rate(220)
    ball.pos = ball.pos + (ball.velocity/ball.mass)*dt
    if not (side > ball.pos.x > -side):
        ball.velocity.x = -ball.velocity.x
    if not (side > ball.pos.y > -side):
        ball.velocity.y = -ball.velocity.y
    if not (side > ball.pos.z > -side):
        ball.velocity.z = -ball.velocity.z
        
    varr.pos = ball.pos - (ball.velocity/ball.mass)*dt
    if not (side > ball.pos.x > -side):
        ball.velocity.x = -ball.velocity.x
    if not (side > ball.pos.y > -side):
        ball.velocity.y = -ball.velocity.y
    if not (side > ball.pos.z > -side):
        ball.velocity.z = -ball.velocity.z

    varr.axis = ball.pos*vscale + (ball.velocity/ball.mass)*dt
    if not (side > ball.pos.x > -side):
        ball.velocity.x = -ball.velocity.x
    if not (side > ball.pos.y > -side):
        ball.velocity.y = -ball.velocity.y
    if not (side > ball.pos.z > -side):
        ball.velocity.z = -ball.velocity.z

    ball2.pos = ball2.pos + (ball2.velocity/ball2.mass)*dt
    if not (side > ball2.pos.x > -side):
        ball2.velocity.x = -ball2.velocity.x
    if not (side > ball2.pos.y > -side):
        ball2.velocity.y = -ball2.velocity.y
    if not (side > ball2.pos.z > -side):
        ball2.velocity.z = -ball2.velocity.z

    varr2.pos = ball2.pos - (ball2.velocity/ball2.mass)*dt
    if not (side > ball2.pos.x > -side):
        ball2.velocity.x = -ball2.velocity.x
    if not (side > ball2.pos.y > -side):
        ball2.velocity.y = -ball2.velocity.y
    if not (side > ball2.pos.z > -side):
        ball2.velocity.z = -ball2.velocity.z

    varr2.axis = ball2.pos*vscale2 + (ball2.velocity/ball2.mass)*dt
    if not (side > ball2.pos.x > -side):
        ball2.velocity.x = -ball2.velocity.x
    if not (side > ball2.pos.y > -side):
        ball2.velocity.y = -ball2.velocity.y
    if not (side > ball2.pos.z > -side):
        ball2.velocity.z = -ball2.velocity.z
        
    ball3.pos = ball3.pos + (ball3.velocity/ball3.mass)*dt
    if not (side > ball3.pos.x > -side):
        ball3.velocity.x = -ball3.velocity.x
    if not (side > ball3.pos.y > -side):
        ball3.velocity.y = -ball3.velocity.y
    if not (side > ball3.pos.z > -side):
        ball3.velocity.z = -ball3.velocity.z

    varr3.pos = ball3.pos - (ball3.velocity/ball3.mass)*dt
    if not (side > ball3.pos.x > -side):
        ball3.velocity.x = -ball3.velocity.x
    if not (side > ball3.pos.y > -side):
        ball3.velocity.y = -ball3.velocity.y
    if not (side > ball3.pos.z > -side):
        ball3.velocity.z = -ball3.velocity.z

    varr3.axis = ball3.pos*vscale3 + (ball3.velocity/ball3.mass)*dt
    if not (side > ball3.pos.x > -side):
        ball3.velocity.x = -ball3.velocity.x
    if not (side > ball3.pos.y > -side):
        ball3.velocity.y = -ball3.velocity.y
    if not (side > ball3.pos.z > -side):
        ball3.velocity.z = -ball3.velocity.z
        
    ball4.pos = ball4.pos + (ball4.velocity/ball4.mass)*dt
    if not (side > ball4.pos.x > -side):
        ball4.velocity.x = -ball4.velocity.x
    if not (side > ball4.pos.y > -side):
        ball4.velocity.y = -ball4.velocity.y
    if not (side > ball4.pos.z > -side):
        ball4.velocity.z = -ball4.velocity.z

    varr4.pos = ball4.pos - (ball4.velocity/ball4.mass)*dt
    if not (side > ball4.pos.x > -side):
        ball4.velocity.x = -ball4.velocity.x
    if not (side > ball4.pos.y > -side):
        ball4.velocity.y = -ball4.velocity.y
    if not (side > ball4.pos.z > -side):
        ball4.velocity.z = -ball4.velocity.z

    varr4.axis = ball4.pos*vscale4 + (ball4.velocity/ball4.mass)*dt
    if not (side > ball4.pos.x > -side):
        ball4.velocity.x = -ball4.velocity.x
    if not (side > ball4.pos.y > -side):
        ball4.velocity.y = -ball4.velocity.y
    if not (side > ball4.pos.z > -side):
        ball4.velocity.z = -ball4.velocity.z