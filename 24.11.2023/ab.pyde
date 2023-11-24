x=1
def setup():
    size(600, 600)
    frameRate(5)
def draw():
    global x
    background(255)
    x=x+0.1
    scale(x)
    # translate(-60,-60)   
    line(300,300,300,200)
    line(250,300,350,200)
    line(250,200,350,300)
     
