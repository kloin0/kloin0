import turtle
import math 
tela = turtle.Screen() 
for c in range(1300):
	vt = c / 40 * math.pi 
	y = (vt * 5 + 5 ) * math.sin(vt)
	x = (vt * 5 + 5 ) * math.cos(vt)
	turtle.goto(x,y)
tela.exitonclick()