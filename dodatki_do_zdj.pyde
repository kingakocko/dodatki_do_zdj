import random
add_library('pdf') 

def setup():
    global img, dodatek, dodatek2
    size(400, 400) # to nie jest proporcja zdjęcia dokumentowego
    img = loadImage("zdjecie.jpg") 
    dodatek= loadImage("usta1.png")
    dodatek2= loadImage("usta2.png")
    beginRecord(PDF, "outzdjecie.pdf")
    

def draw():
    image(img,0,0,height,width)
    if keyPressed:
        if key==('o'):
            image(dodatek,140,250,height-290,width-330)
            endRecord()
        if key==('k'):
           image(dodatek2,140,250,height-290,width-330)
           endRecord()
        if key==('n'):
            image(img,0,0,height,width)
            endRecord()

def mousePressed():
    exit()

# trochę zamieszałaś, oczyściłam kod ze zbędnych linijek zachowując działanie, przyjrzyj się zmianom
#1,25pkt
