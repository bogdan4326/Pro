value=1
x = 1
col1 = color(139,71,28)
col2 = color(139,71,28)
def setup():
    size(1000,600)
def draw():
    fill(255)
    textSize(20)
    text(u"Ты выграл", 700,300)3
    global x,value, col1, col2
    fill(col1)
    rect(150,50,320,500)
    
    fill(col2)
    rect(500,50,320,500)
    
    ellipse(220, 290, 60, 60)
    ellipse(580, 290, 60, 60)
# def mouseClicked(): 
#     global value
#     rect(150,50,320,500)
#     rect(500,50,320,500)
#     if value == 0:
#         value = 255
#     else:
#         value = 0
def mouseClicked(): 
    global value, col1, col2
    if value == 0:
        value = 255
    else:
        value = 0
    
    if mouseX > 150 and mouseX < 470 and mouseY > 50 and mouseY < 550:
        col1 = color(0,0,0)
        
    if mouseX > 500 and mouseX < 820 and mouseY > 50 and mouseY < 550:
        col2 = color(0,0,0)
    # rect(500,50,320,500)
