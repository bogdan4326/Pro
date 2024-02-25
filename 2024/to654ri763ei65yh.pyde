x=1

def setup():
    
    size(1000,1000) 
    
def draw():
    global x
    background(255)
    x=x+2
    frameRate(5)
    translate(x,0)
    fill(22, 21, 255)
    rect(430, 450, 200, 200)
    fill(10)
    rect(370,450, 80, 200)
    fill(20)
    rect(630, 450, 80, 200)
    fill(30)
    rect(370, 450, 80, 60)
    fill(40)
    rect(630, 450, 80, 60)
    fill(50)
    rect(450, 650, 80, 170)
    fill(60)
    rect(550, 650, 80, 170)
    fill(70)
    rect(490, 350, 100, 100)
    strokeWeight(5)
    point(560, 390)
    point(520, 390)
    strokeWeight(10)
    point(540, 410)
