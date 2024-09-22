import Image
photo = Image.open('test.png')
photo = photo.convert('RGB')

w = photo.size[0] 
h = photo.size[1]
rgbval=""
for y in range(0, h):
    for x in range(0, w):
        RGB = photo.getpixel((x,y))
        R,G,B = RGB  
        rgbval+= "("+str(R)+","+str(G)+","+str(B)+")"+" "
    print widthtext
    widthtext=""
