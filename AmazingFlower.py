from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)

for i in range(16):
    begin_fill()
    for j in range(10):
        c = colorsys.hsv_to_rgb(i/15,j/20,1)
        color(c)
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
        circle(40,24)
        end_fill()
        
done()
        
