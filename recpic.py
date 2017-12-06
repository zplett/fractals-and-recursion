#Zac Plett
#recpic.py
#9 October 2016
#
#I have adhered to the Honor Code on this assignment.

import picture

#Prompts the user to input the information needed to display the fractal.
#Makes calls to all other functions.
def main():
    
    print("Enter '1' to select bubbles.")
    print("Enter '2' to select carpet.")
    print("Enter '3' to select gasket.")
    print("Enter '4' to select snowflake.")
    
    option = eval(input("Which would you like to select?: "))
    
    done = False
    
    if option == 1:
        
        size = eval(input("Please enter the size of the canvas: "))
        depth = eval(input("Please enter the depth: "))
        
        pic = picture.Picture(size,size)
        pic.setFillColor(255,140,0)
        pic.drawRectFill(0,0,size,size)
        pic.setFillColor(0,0,255)
        pic.setOutlineColor(0,0,255)
        
        bubbles(size,depth,0,0,size,size,pic)
    
    if option == 2:
        
        size = eval(input("Please enter the size of the canvas: "))
        depth = eval(input("Please enter the depth: "))
        
        pic = picture.Picture(size,size)
        pic.setFillColor(0,255,0)
        pic.drawRectFill(0,0,size,size)
        pic.setFillColor(255,0,0)
        pic.setOutlineColor(255,0,0)
        
        carpet(size,depth,size//2, size//2, pic)
        
    if option == 3:
        
        size = eval(input("Please enter the size of the canvas: "))
        depth = eval(input("Please enter the depth: "))
        
        pic = picture.Picture(size,size)
        pic.setFillColor(255,255,0)
        pic.drawRectFill(0,0,size,size)
        pic.setFillColor(0,0,255)
        pic.setOutlineColor(0,0,255)
        
        gasket(depth, size//2, 0, 0, size, size, size, pic)
        
    if option == 4:
        
        size = eval(input("Please enter the size of the canvas: "))
        depth = eval(input("Please enter the depth: "))
        
        pic = picture.Picture(size,size)
        pic.setFillColor(138,43,226)
        pic.drawRectFill(0,0,size,size)
        pic.setFillColor(127,255,0)
        pic.setOutlineColor(127,255,0)
        
        pic.setPenWidth(2)
        pic.setPosition(size//5, 2*(size//3))
        
        pic.rotate(300)
        snowflake((2*size)//3, depth, pic)
        pic.rotate(120)
        snowflake((2*size)//3, depth, pic)
        pic.rotate(120)
        snowflake((2*size)//3, depth, pic)
    
    pic.display()
    input()

#Displays the bubble fractal. 
def bubbles(size, depth, x1, y1, x2, y2, pic):
   
    if depth < 1:
        return 0
   
    else:
        newX = (x1+x2)//2
        newY = (y1+y2)//2
        r = size//4
        
        pic.drawCircleFill(newX,newY,r)
        
        bubbles(size//2, depth-1, x1, y1, (x1+x2)//2, (y1+y2)//2, pic)
        bubbles(size//2, depth-1, x1, (y1+y2)//2, (x1+x2)//2, y2, pic)
        bubbles(size//2, depth-1, (x1+x2)//2, y1, x2, (y1+y2)//2, pic)
        bubbles(size//2, depth-1, (x1+x2)//2, (y1+y2)//2, x2, y2, pic)

#Displays the carpet fractal. 
def carpet(size, depth, x, y, pic):
    
    if depth < 1:
        return 0
    else:
        
        newS = size//3
        
        pic.drawRectFill(x-(newS//2),y-(newS//2),newS,newS)
        
        carpet(newS, depth-1, x-newS, y-newS, pic)
        carpet(newS, depth-1, x, y-newS, pic)
        carpet(newS, depth-1, x+newS, y-newS, pic)
        carpet(newS, depth-1, x+newS, y, pic)
        carpet(newS, depth-1, x+newS, y+newS, pic)
        carpet(newS, depth-1, x, y+newS, pic)
        carpet(newS, depth-1, x-newS, y+newS, pic)
        carpet(newS, depth-1, x-newS, y, pic)
        
        
#Displays the gasket fractal.
def gasket(depth, a, b, c, d, e, f, pic):
    
    if depth < 0:
        return 0
    
    elif depth == 1:
    
        pic.drawPolygonFill([(a,b), (c,d), (e,f)])
    
    else:
        
        gasket(depth-1, a, b, (c+a)//2, (b+d)//2, (a+e)//2, (b+f)//2, pic)
        gasket(depth-1,(c+a)//2, (b+d)//2, c, d, (c+e)//2, (d+f)//2, pic )
        gasket(depth-1, (a+e)//2, (b+f)//2,(c+e)//2, (d+f)//2, e, f, pic)
    
#Displays the snowflake fractal.
def snowflake(length, depth, pic):
    
    if depth < 1:
        return 0
        
    elif depth == 1:
        
        pic.drawForward(length)
        
    else:
        
        newL = length//3
        
        snowflake(newL, depth-1, pic)
        pic.rotate(300)
        snowflake(newL, depth-1, pic)
        pic.rotate(120)
        snowflake(newL, depth-1, pic)
        pic.rotate(300)
        snowflake(newL, depth-1, pic)
        
    
main()