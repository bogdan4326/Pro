# Отладка 3
# Найдите и исправьте ошибку(-и), чтобы код заработал

def setup():
    size(600,600)
    frameRate(2)
    
def draw():
    background(80, 80, 160)
    triangle(200,random(200,400), random(200,400),400, 400,random(200,400))
