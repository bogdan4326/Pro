
def setup():
    size(600,600)
    background(0)
    
def draw():

    stroke(random (0,200),random(0,200),random(0,200))
    strokeWeight(5)
    point(random(0,600),random(0,600))
    if frameCount%400 == 0:
        background(0)

    
