img = 0
x=1
def setup():
    size(500,500)
    global img
    img = loadImage("data.jpeg")
    imageMode(CENTER)
    
     
def draw():
    global x
    x=x+1
    translate(x,1)
    rotate(radians(x))
    image(img,100,100,300,300)
