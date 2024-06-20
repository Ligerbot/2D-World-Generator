import turtle
# importing libraries 
import cv2 
import numpy as np 
from turtle import Screen, Turtle
import time
import random
turtle.setup(2560, 1600)
turtle.penup()
turtle.write("Generating World",font=('Arial',10,'normal'))
turtle.goto(0,-20)
turtle.write("(My favorite music)")
turtle.goto(0,0)
print("Starting game...")
print("Rendering world... This may take a min")
turtle.speed('fastest')
block_width = 5
block_height = 5
turtle_size_move = 20
#no layers
#layer_height = 1
world = []
def air():
	turtle.color("")
	for i in range(block_width):
		turtle.stamp()
		turtle.forward(turtle_size_move)
		world.append(0)
	turtle.forward(turtle_size_move)
#def cutscreen(vid_num):
#	cutscreen_trigger = open('vid_trigger', 'w')
#	file.write(vid_num)
#	file.close()
def stone():
	turtle.color("gray")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(block_height):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,5)
			if r == 1:
				turtle.color("gray")
			elif r == 2:
				turtle.color("DarkGrey")
			elif r == 3:
				turtle.color("DarkGray")
			elif r == 4:
				turtle.color("azure4")
			elif r == 5:
				turtle.color("AntiqueWhite4")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.left(90)
	turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)
def iron():
	turtle.color("gray")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(block_height):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,9)
			if r == 1:
				turtle.color("LightSteelBlue4")
			elif r == 2:
				turtle.color("DarkOrange4")
			elif r == 3:
				turtle.color("chocolate2")
			elif r == 4:
				turtle.color("orange4")
			elif r == 5:
				turtle.color("gray")
			elif r == 6:
				turtle.color("gray30")
			elif r == 7:
				turtle.color("azure4")
			elif r == 8:
				turtle.color("AntiqueWhite4")
			elif r == 9:
				turtle.color("cornsilk4")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.left(90)
	turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)
def gold():
	turtle.color("gray")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(block_height):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,7)
			if r == 1:
				turtle.color("gray")
			elif r == 2:
				turtle.color("DarkGrey")
			elif r == 3:
				turtle.color("DarkGray")
			elif r == 4:
				turtle.color("azure4")
			elif r == 5:
				turtle.color("AntiqueWhite4")
			if r == 6:
				turtle.color("gold1")
			if r == 7:
				turtle.color("goldenrod1")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.left(90)
	turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)

def wood():
	turtle.color("SaddleBrown")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(block_height):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,7)
			if r == 1:
				turtle.color("sienna")
			elif r == 2:
				turtle.color("sienna")
			elif r == 3:
				turtle.color("tan4")
			elif r == 4:
				turtle.color("tan4")
			elif r == 5:
				turtle.color("sienna4")
			if r == 6:
				turtle.color("SaddleBrown")
			if r == 7:
				turtle.color("sienna4")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.left(90)
	turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)

def dirt():
	turtle.color("sienna")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(block_height):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,7)
			if r == 1:
				turtle.color("sienna")
			elif r == 2:
				turtle.color("tan4")
			elif r == 3:
				turtle.color("tan4")
			elif r == 4:
				turtle.color("tan3")
			elif r == 5:
				turtle.color("sienna4")
			if r == 6:
				turtle.color("SaddleBrown")
			if r == 7:
				turtle.color("sienna")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.left(90)
	turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)
def grass():
	turtle.color("sienna")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(3):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,7)
			if r == 1:
				turtle.color("sienna")
			elif r == 2:
				turtle.color("tan4")
			elif r == 3:
				turtle.color("tan4")
			elif r == 4:
				turtle.color("tan3")
			elif r == 5:
				turtle.color("sienna4")
			if r == 6:
				turtle.color("SaddleBrown")
			if r == 7:
				turtle.color("sienna")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	for i in range(block_width):
		turtle.stamp()
		r = random.randint(0,3)
		if r == 0:
			turtle.color("LimeGreen")
		if r == 1:
			turtle.color("OliveDrab")
		if r == 2:
			turtle.color("green4")
		if r == 3:
			turtle.color("sienna")
		turtle.forward(turtle_size_move)
	turtle.left(180)
	turtle.forward(block_width*turtle_size_move)
	turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.color("LimeGreen")
	for i in range(block_width):
		turtle.stamp()
		r = random.randint(0,3)
		if r == 0:
			turtle.color("LimeGreen")
		if r == 1:
			turtle.color("OliveDrab")
		if r == 2:
			turtle.color("green4")
		if r == 3:
			turtle.color("ForestGreen")
		turtle.forward(turtle_size_move)


	#turtle.forward(turtle_size_move)
	#turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move-turtle_size_move)
	turtle.left(90)
	#turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)

def leaf():
	turtle.color("DarkGreen")
	#turtle.goto(x,y)
	#turtle.setfillopacity(50)
	for i in range(block_height):
		for i in range(block_width):
			turtle.stamp()
			r = random.randint(1,7)
			if r == 1:
				turtle.color("DarkOliveGreen")
			elif r == 2:
				turtle.color("DarkOliveGreen3")
			elif r == 3:
				turtle.color("DarkGreen")
			elif r == 4:
				turtle.color("DarkGreen")
			elif r == 5:
				turtle.color("DarkGreen")
			if r == 6:
				turtle.color("chartreuse3")
			if r == 7:
				turtle.color("green4")
			turtle.forward(turtle_size_move)
		turtle.left(180)
		turtle.forward(block_width*turtle_size_move)
		turtle.right(90)
		turtle.forward(turtle_size_move)
		turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.left(90)
	turtle.forward(turtle_size_move*block_width-turtle_size_move)
	world.append(1)


def rock():
	stone()
	turtle.forward(block_width*turtle_size_move-turtle_size_move)
	turtle.left(90)
	#turtle.forward(block_width*turtle_size_move)
	stone()
	stone()
	turtle.right(90)
	turtle.forward(turtle_size_move)
	turtle.right(90)
	turtle.forward(turtle_size_move)
	stone()
	stone()
	turtle.forward(-1*turtle_size_move)
	turtle.left(90)
	turtle.forward(block_width*turtle_size_move)
	stone()
def tree(x,y):
	turtle.backward(turtle_size_move)
	turtle.left(90)
	r = random.randint(5,6)
	#turtle.backward(turtle_size_move)
	for i in range(r):
		wood()
	if r == 6:
		wood()
	turtle.right(180)
	turtle.forward(r*block_height*turtle_size_move-turtle_size_move)
	turtle.goto(x-(3*block_width*turtle_size_move),y+(2*block_height*turtle_size_move))
	if random.randint(1,2) == 2:
                turtle.goto(turtle.xcor(), int(turtle.ycor()) - random.randint(-1,1) * block_height*turtle_size_move)
                turtle.setheading(0)
                leaf()
                leaf()
                leaf()
                leaf()
                leaf()

	turtle.setheading(0)
	leaf()
	leaf()
	leaf()
	leaf()
	leaf()
	if r == 6:
		turtle.goto(x-(3*block_width*turtle_size_move),y+(2*block_height*turtle_size_move)+block_height*turtle_size_move*2)
		leaf()
		leaf()
		leaf()
		leaf()
		leaf()
	if r == 6:
		turtle.goto(x-(2*block_width*turtle_size_move),y+(4*block_height*turtle_size_move)+block_height*turtle_size_move*2)
	else:
		turtle.goto(x-(2*block_width*turtle_size_move),y+(4*block_height*turtle_size_move))
	leaf()
	leaf()
	leaf()
	turtle.goto(x,y)


def render_world(seed):
	turtle.left(180)
	turtle.forward(1280)
	turtle.left(90)
	turtle.forward(800-turtle_size_move)
	turtle.left(90)
	turtle.shape("square")
#	cutscreen(1)
	for i in range(5):
		for i in range(26):
			r = random.randint(0, 6)
			if r == 0:
				stone()
			if r == 1:
				iron()
			if r == 2:
				gold()
			if r == 3:
				iron()
			if r == 4:
				stone()
			if r == 5:
				stone()
			if r == 6:
				stone()
		turtle.left(180)
		turtle.forward(2560+turtle_size_move+20)
		turtle.right(90)
		turtle.forward(block_height*turtle_size_move)
		turtle.right(90)
		#	cutscreen(0)
	for i in range(3):
		for i in range(26):
			r = random.randint(0,7)
			if r == 0:
				dirt()
			if r == 1:
				stone()
			if r == 2:
				dirt()
			if r == 3:
				dirt()
			if r == 4:
				dirt()
			if r == 5:
				dirt()
			if r == 6:
				dirt()
			if r == 7:
				dirt()
		turtle.left(180)
		turtle.forward(2560+turtle_size_move+20)
		turtle.right(90)
		turtle.forward(block_height*turtle_size_move)
		turtle.right(90)
	for i in range(26):
		grass()
	turtle.left(180)
	turtle.forward(2560+turtle_size_move+20)
	turtle.right(90)
	turtle.forward(block_height*turtle_size_move)
	turtle.right(90)
	turtle.forward(block_width*turtle_size_move*3)
	for i in range(10):
		r = random.randint(0,6)
		if r == 0:
			turtle.forward(block_width*turtle_size_move)
		if r == 1:
			turtle.forward(2*(block_width*turtle_size_move))
		if r == 2:
			tree(turtle.xcor(),turtle.ycor())
			turtle.forward(200)
		if r == 3:
			tree(turtle.xcor(),turtle.ycor())
			turtle.forward(3*(block_width*turtle_size_move))
		if r == 4:
			turtle.forward(block_width*turtle_size_move)
			rock()
			#turtle.forward(block_width*turtle_size_move)
		if r == 5:
			tree(turtle.xcor(),turtle.ycor())
			turtle.forward(3*(block_width*turtle_size_move))
		if r == 6:
			tree(turtle.xcor(),turtle.ycor())
			turtle.forward(3*(block_width*turtle_size_move))
render_world(1)
time.sleep(10)

