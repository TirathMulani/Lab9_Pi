from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw  

def clearScreen(lcd):  
    lcd.clear()
    lcd.show()

def displayText(text, lcd, x, y):  
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w): 
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)  
    lcd.show()

def dispObj(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)
            if x2 == 1:
                pixel = 1    
            else:
                pixel = 0
            lcd.set_pixel(xp, y, pixel)
            xp = xp + 1
        y = y + 1
        lcd.set_pixel(xp, y , pixel)
        xp = x
    lcd.show()

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

f1 =  [ 
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

x_start = int(input("X- coordinate between 0 - 127: "))
y_start = int(input("Y- coordinate between 0 - 63: "))
#dispObj(pm,x_start,y_start)
dispObj(f1,x_start,y_start)
