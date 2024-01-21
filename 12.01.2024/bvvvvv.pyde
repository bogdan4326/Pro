x=0
def setup():
    size(500,500)
    #noStroke()
    #strokeWeight(5)       
def draw():
    global x
    x=x+45
    background(0)
    #translate(150,150)
    stroke(random(0,200),random(0,200),random(0,200),random(0,200))
    rectMode(CENTER)
    rotate(radians(x))
    triangle(250,250,100 , 2, 30, 3)
    

    
