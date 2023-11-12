x=500

def setup():
    size(600, 600)
    background(210,240,255)
    noStroke()
    
def draw():
    global x
    x=x+5
    translate(-20,-30)
    fill(190,50,70)
    triangle(500,400, 550,325, 600,400),random(0,200),random(0,200),random(0,200)
    fill(255,190,10)
    rect(515,400, 70,70),random(0,200),random(0,200),random(0,200)   
    fill(85,85,85)
    rect(535,420, 30,50),random(0,200),random(0,200),random(0,200)
