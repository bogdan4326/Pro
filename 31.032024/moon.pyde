pos=0
def setup():
    size(500,500)
    
    
def draw():
    global pos
    pos=pos+5
    ellipse(250,250,150,150)
    ellipse(250,290,80,60)
    ellipse(250,399,150,150)
