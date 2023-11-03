x=500

def setup():
    size(1000,1000)
    
def draw():
    global x
    x=x+5
    strokeWeight(10)
    point(500,500)
    point(x,x)
    point(500,500)
    point(500,500)
    
