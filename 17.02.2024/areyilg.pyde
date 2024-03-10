z=1

def setup():
    size(600,600)
    
def draw():
    global z 
    z=z+1
    translate(200, 300)
    scale(z)
    #background(255)
    ellipse(30, z, 30,30)
    if z >= 50:
        z = 1

    print( z)
