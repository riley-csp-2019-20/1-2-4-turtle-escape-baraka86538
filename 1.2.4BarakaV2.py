import turtle as trtl
import random
ok = trtl.Turtle()
bk = trtl.Turtle()
ok.speed(0)
ok.pensize(5)
ok.ht()
bk.pencolor("blue")
count = 250 
wall_width = 8
door_width = 22
for i in range(25):

    if i < 20:
        door = random.randint(wall_width, count - door_width*2)
        barrier =  random.randint(wall_width, count - door_width*2)
        if door < barrier:
                
            ok.forward(door)
            ok.penup()
            ok.forward(door_width)
            ok.pendown() 
            ok.forward(barrier - door - door_width)
            

            ok.right(90)
            ok.forward(wall_width*2)
            ok.back(wall_width*2)
            ok.left(90)
            
            ok.forward(count - barrier)


        else:
            ok.forward(barrier)

            ok.right(90)
            ok.forward(wall_width*2)
            ok.backward(wall_width*2)
            ok.left(90)

            ok.forward(door - barrier)
            ok.penup()
            ok.forward(door_width)
            ok.pendown()

            ok.forward(count - door - door_width)
        
        
    ok.right(90)
    count = count - wall_width



def bk_up():
    bk.setheading(90)
    bk.forward(10)

def bk_down():
    bk.setheading(270)
    bk.forward(10)

def bk_right():
    bk.setheading(0)
    bk.forward(10)

def bk_left():
    bk.setheading(180)
    bk.forward(10)







wn = trtl.Screen()
wn.onkeypress(bk_up,"Up")
wn.onkeypress(bk_down,"Down")
wn.onkeypress(bk_right,"Right")
wn.onkeypress(bk_left,"Left")



wn.listen()
wn.mainloop()





