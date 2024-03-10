z=10
v=1
def setup():
    size(600,400)
    
def draw():
    global z 
    z=z+5
    global v
    v=v+5
    background(255)
    ellipse(z, v, 30,30)
    if z>= 600:
        z = 0
    if v>= 400:
        v = 0
    print(v, z)
