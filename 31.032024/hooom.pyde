pos=0
def setup():
    size(500,500)
    frameRate(4)
    
def draw():
    background(204)
    global pos
    pos=pos+5
    fill(random(0,200))
    line(pos,20,pos,80)
    if pos > width:
        pos = 0
        fill (100)
