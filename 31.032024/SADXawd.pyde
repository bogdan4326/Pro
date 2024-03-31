x = 1
mode = "r"
def setup():
    size(1000,1000)
    strokeWeight(90)
def draw():
    global x, mode
    stroke(random(255))
    if mode == "r":
       x=x+1
    if mode == "l":
       x=x-1
        
    if x > 1000:
       mode = "l"
    if x < 0:
       mode = "r"
    point(200, x)
