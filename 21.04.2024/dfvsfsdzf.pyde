value=1
x = 1
def setup():
    size(1000,1000)
def draw():
    global x,value
    line(mouseX,  mouseY, pmouseX,  pmouseY)
def mouseClicked(): 
        background(random(255),random(255),random(255))
        
    
