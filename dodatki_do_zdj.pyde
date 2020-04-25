import random
add_library('pdf') 

def setup():
    global img 
    size(400, 400) 
    img = loadImage("zdjecie.jpg") 
    beginRecord(PDF, "outzdjecie.pdf")
    

def draw():
    if keyPressed:
        if key==('o'):
            img= loadImage("zdjecie.jpg")
            image(img,0,0,height,width)
            global dodatek
            dodatek= loadImage("usta1.png")
            beginRecord(PDF,"outusta1.pdf")
            image(dodatek,140,250,height-290,width-330)
            endRecord()
        if key==('k'):
           img= loadImage("zdjecie.jpg")
           image(img,0,0,height,width)
           global dodatek2
           dodatek2= loadImage("usta2.png")
           beginRecord(PDF,"outusta2.pdf")
           image(dodatek2,140,250,height-290,width-330)
           endRecord()
        if key==('n'):
            clear() 
            img= loadImage("zdjecie.jpg")
            image(img,0,0,height,width)
            endRecord()

def mousePressed():
    exit()
