x=400
def setup():
    size(600, 600)
    
def draw():
    global x
    x=x+5
    
    strokeWeight(10)
    #ellipse(445,331,20,1)
    fill(221,222,175)
    ellipse(300,300, 180,180)
    triangle(390,310, x,330, 380,342)
    
    fill(0,0,0)
    point(360, 300)
    fill(250,0,0)
    triangle(380,255, 300,100, 220,255)
    
