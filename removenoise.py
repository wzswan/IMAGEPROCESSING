#coding:utf-8  
import sys,os  
from PIL import Image,ImageDraw  
  
#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换  
#该函数也可以改成RGB判断的,具体看需求如何  
def getPixel(image,x,y):  
    L = image.getpixel((x,y))  
     
    
    leftpixel = image.getpixel((x - 1,y))
    rightpixel = image.getpixel((x + 1,y))
    uppixel = image.getpixel((x, y + 1 ))
    downpixel = image.getpixel((x,y - 1))
    
    G = (leftpixel + rightpixel + uppixel + downpixel)/4
    
    if (L - G) > 10:
        L = G
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
    image.save("C:/Users/wzswan/Pictures/result.jpg")  
  
  
if __name__ == '__main__':  
    main() 