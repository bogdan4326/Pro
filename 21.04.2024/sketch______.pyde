pos=0
x=2
def setup():
    size(500,500)
    
    
def draw():
    global pos ,x
    pos=pos+5
    fill(214,173,123)
    ellipse(250,250,150,150)
    fill(0)
    ellipse(250,290,40,20)
    fill(214,173,123)
    ellipse(250,399,150,150)
    ellipse(160,380,90,50)
    ellipse(190,200,60,60)
    ellipse(310,200,60,60)
    strokeWeight(5)
    point(280,250)
    point(220,250)
    scale(x)
    ellipse(350,380,90,50)
    
    
    
    
