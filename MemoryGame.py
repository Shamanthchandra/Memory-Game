# implementation of card game - Memory

import simplegui
import random
import math

list1 = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
random.shuffle(list1)
point = [25,75,125,175,225,275,325,375,425,475,525,575,625,675,725,775]
j=0
extended = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
always = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mark = []
count = 0
turn = 0

# helper function to initialize globals
def new_game():
    global list1,point,j,extended,mark,count,turn,always
    list1 = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
    random.shuffle(list1)
    point = [25,75,125,175,225,275,325,375,425,475,525,575,625,675,725,775]
    j=0
    extended = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    always = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    mark = []
    count = 0
    turn = 0

def distance(p,q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
     
# define event handlers
def mouseclick(pos):
    global mark,extended,point,count,x,y,temp,turn
    # add game state logic here
    post = list(pos)
    for poi in point:
        if distance([poi,105],post) <= 20:
            count += 1
            mark.append(point.index(poi))
            temp = mark.pop()
            mark.append(temp)
    
    if extended[temp] == 1:
        if count % 2 == 1:
            turn -= 1
            
    extended[temp] = 1
    
    if count % 2 == 0:
        x = mark.pop()
        y = mark.pop()
        
    
    if count != 1:
        if count % 2 == 1:
            turn += 1
            if list1[x] != list1[y]:
                extended[x] = 0
                extended[y] = 0
            else:
                always[x] = 1
                always[y] = 1
    elif count == 1:
        turn += 1
        
    for z in range(16):
        if always[z] == 1:
            extended[z] = 1
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global j,turn
    j = 0
    canvas.draw_circle((30,100),20,2,"Black","Green")
    canvas.draw_circle((80,100),20,2,"Black","Green")
    canvas.draw_circle((130,100),20,2,"Black","Green")
    canvas.draw_circle((180,100),20,2,"Black","Green")
    canvas.draw_circle((230,100),20,2,"Black","Green")
    canvas.draw_circle((280,100),20,2,"Black","Green")
    canvas.draw_circle((330,100),20,2,"Black","Green")
    canvas.draw_circle((380,100),20,2,"Black","Green")
    canvas.draw_circle((430,100),20,2,"Black","Green")
    canvas.draw_circle((480,100),20,2,"Black","Green")
    canvas.draw_circle((530,100),20,2,"Black","Green")
    canvas.draw_circle((580,100),20,2,"Black","Green")
    canvas.draw_circle((630,100),20,2,"Black","Green")
    canvas.draw_circle((680,100),20,2,"Black","Green")
    canvas.draw_circle((730,100),20,2,"Black","Green")
    canvas.draw_circle((780,100),20,2,"Black","Green")
    
    canvas.draw_text("Turns = "+str(turn),[350,40],25,"White")
    
    for i in range(16):
        if extended[i] == 1:
            canvas.draw_text(str(list1[i]),[point[i],105],25,"White")
   

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 200)
frame.add_button("Reset", new_game)
frame.set_canvas_background("Violet")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
