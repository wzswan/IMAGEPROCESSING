#coding:utf-8  
import sys,os  
from PIL import Image,ImageDraw  
  
#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换  
#该函数也可以改成RGB判断的,具体看需求如何  
def getPixel(image,x,y):  
    L = image.getpixel((x,y))  
     
    
    leftpixel = image.getpixel((x - 1,y))
    leftuppixel = image.getpixel((x - 1,y + 1))
    leftdownpixel = image.getpixel((x - 1,y - 1))
    rightpixel = image.getpixel((x + 1,y))
    rightuppixel = image.getpixel((x + 1,y + 1))
    rightdownpixel = image.getpixel((x + 1,y - 1))
    uppixel = image.getpixel((x, y + 1 ))
    downpixel = image.getpixel((x,y - 1))
    
    G = (leftpixel + rightpixel + uppixel + downpixel + leftuppixel + leftdownpixel + rightuppixel +    rightdownpixel + L)/9
    
    b = sorted([leftpixel,rightpixel,uppixel,downpixel,leftuppixel,leftdownpixel,rightuppixel,rightdownpixel,L])
    A = (b[2] + b[3] + b[4] + b[5] + b[6])/5
    if (L - G) > 10:
        L = A
    return L
        
    
   
   
def clearNoise(image):  
    draw = ImageDraw.Draw(image) 
    for x in xrange(1,image.size[0] - 1):  
        for y in xrange(1,image.size[1] - 1):  
            color = getPixel(image,x,y)  
            if color != None:  
                draw.point((x,y),color)  
  
 #测试代码  
def main():  
    #打开图片  
    image = Image.open("C:/Users/wzswan/Pictures/1.jpg")  
  
    #将图片转换成灰度图片
    image = image.convert("L")  
  
    #去噪,G = 50,N = 4,Z = 4  
    clearNoise(image)  
  
    #保存图片  
    image.save("C:/Users/wzswan/Pictures/resul.jpg")  
  
  
if __name__ == '__main__':  
    main() 