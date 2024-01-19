x=0
def setup():
    size(300,300)    
def draw():
    global x
    x=x+5
    frameRate(5)
    background(0)
    translate(150,150)
    rectMode(CENTER)
    rotate(radians(x))
    ellipse(x,20, 80,60)
