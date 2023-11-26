x=1
def setup():
    size(600, 600)
    background(0)
    frameRate(5)
     
def draw():
    global x
    x=x-0.1
    scale(x)
    rect(60,60, 300,300)
    rect(400,65, 300,300)
