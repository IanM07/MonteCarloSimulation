#Import all needed libraries
import random
import turtle
import math

#Creates turtle for drawing and initializes radius and length variables
draw = turtle
draw.hideturtle()
draw.speed(0)
radius = random.uniform(1,200)
length = radius * 2

#Draws a Circle
draw.up()
draw.setposition(radius,0)
draw.down()
draw.circle(radius)

#Draws a Square around the circle
draw.up()
draw.setposition(0,0)
draw.down()
draw.fd(length)
draw.lt(90)
draw.fd(length)
draw.lt(90)
draw.fd(length)
draw.lt(90)
draw.fd(length)
draw.lt(90)

#Find the area of the circle and then the square
ArCircle = math.pi * radius ** 2
ArSquare = length* length

#Calculate the probability of a point falling in the circle
Pcircle = ArCircle / ArSquare
print("--------------------------------------------")
print("Radius of the Circle:", radius)
print("Length of the Square:", length)
print("Area of the circle:", ArCircle)
print("Area of the square:", ArSquare)
print("Probability of a point in the circle:", '{:.2%}'.format(Pcircle))
print("--------------------------------------------")

#Start the trials
trialnum = 1
while trialnum < 11:
    hits = 0
    print("Trial Number", trialnum)
    
    numpoints = 1000000
    while numpoints > 0: 
        #Generate the random x and y coordinates within the square
        xcoord = random.uniform(0, length)
        ycoord = random.uniform(0, length)
        
        '''#Draw the dots created
        if trialnum == 10:
            draw.up()
            draw.setposition(xcoord,ycoord)
            draw.down()
            draw.dot(4)'''
        
        #Check to see if the x and y coordinates are inside the circle
        dist = math.sqrt((xcoord)**2 + (ycoord)**2)
        if dist <= radius:
            hits = hits + 4
                   
        numpoints = numpoints - 1
    
    trialnum = trialnum + 1
    #Print the summary of each trial
    print("Number of hits:",hits)
    #Calculate the percentage of hits
    phits = hits / 1000000
    print("Percentage of hits:",'{:.2%}'.format(phits))
    avgnumhit = 0
    avgnumhit = avgnumhit + hits
    print("---------------")
avgnumhit = avgnumhit / 10
print ("There were", avgnumhit, "hits on average.")


