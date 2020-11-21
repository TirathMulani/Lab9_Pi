from gfxhat import lcd,  fonts, backlight, touch
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

def etchaske(x,y):
    backlight.set_pixel(0, 0, 255, 0)
    backlight.show()
    while True:
        key = getchar()
        print(key)
        lcd.set_pixel(x,y,1)
        lcd.show()
        if key == 's':
            clearScreen(lcd)
        elif key == 'w':
            y = y - 1
            if y == 0:
                y = 63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == 'x':
            y = y + 1
            if y == 63:
                y=0
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif key == 'a':
            x = x - 1
            if x == 0:
                x=127
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif key == 'd':
            x = x + 1
            if x == 127:
                x=0
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif key == 'q':
            lcd.clear()
            lcd.show()
            exit()
        else:
            print("Not a valid input")

x_start = int(input("X- coordinate between 0 - 127: "))
y_start = int(input("Y- coordinate between 0 - 63: "))
displayText("EtchSketch",lcd,20,20)
etchaske(x_start, y_start)