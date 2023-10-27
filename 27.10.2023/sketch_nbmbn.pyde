def setup():
    background(0)
    size(600,600)
    
    
def draw():
    fill(random(0,255),random(0,255),random(0,255))
    translate(random(-290,290),random(-290,290))
    ellipse(300,300,random(1,5),random(1,5))
