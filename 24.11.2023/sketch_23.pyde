x=1
def setup():
    size(600, 600)
    frameRate(2)
     
def draw():
    x=1
    global r
    x=x+0.1
    background(100)
    translate(300,300)
    scale(x)
    ellipse(0,70,200,200)
    ellipse(0,-100,150,150)
    ellipse(0,-200,100,100)
    
