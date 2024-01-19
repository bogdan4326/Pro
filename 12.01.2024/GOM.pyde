x=0
def setup():
    size(300,300)
    noStroke()
    strokeWeight(5)       
def draw():
    global x
    x=x+5
    #background(0)
    translate(150,150)
    stroke(random(0,200),random(0,200),random(0,200),random(0,200))
    rectMode(CENTER)
    rotate(radians(x))
    line(100,100, 2,2)
