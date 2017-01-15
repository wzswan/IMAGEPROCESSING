from PIL import Image, ImageFont, ImageDraw

im = Image.new('RGB', (255,255), (255,255,255))
dr = ImageDraw.Draw(im)
        # dr.rectangle(((0+(j)*100,0+(j)*100),(100+(j)*100, 100+(j)*100)), fill="blue", outline = "black")
for i in range(0,127):
    #for j in range(0,255):
        print([(0+i*2,255),(1+i*2,255)])
        dr.rectangle([(255,0+i*2),(255,100+1+i*2)], fill="blue", outline = "black")
        im.show()