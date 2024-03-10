z=20

def setup():
    size(600,600)
    
def draw():
    global z 
    z=z+5
    fill(z)
    ellipse(300, 300, 30,30)
    if z >= 600:
        z = 0
