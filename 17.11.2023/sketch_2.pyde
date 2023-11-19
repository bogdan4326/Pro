x=500
def setup():
    size(600, 600)
    
def draw():
    
    global x
    x=x-5
    scale(2)
    translate(-60,-60)   
    line(300,300,300,200)
    line(250,300,350,200)
    line(250,200,350,300)
