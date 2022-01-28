import unicornhathd as uni
import time
from PIL import Image, ImageDraw, ImageFont


class OutputFramework:

    @staticmethod
    def setWindow(ausgabe: list, rotation = 90):
        """
        Zeigt eine Ausgabe an.
        :param ausgabe: Liste mit Dimensionen (16,16,3) (r (0 - 255) , g (0 - 255), b (0 - 255))
        """
        for x in range(len(ausgabe)):
            for y in range(len(ausgabe[x])):
                uni.set_pixel(x, y, ausgabe[x][y][0], ausgabe[x][y][1], ausgabe[x][y][2])

        uni.set_rotation(rotation)
        uni.show()

    @staticmethod
    def setPixel(x: int, y: int, r: int, g: int, b: int, rotation = 90):
        """
        Setzt einzelne Pixel, werden aber erst mit .show angezeigt
        :param x: x Position des Pixels
        :param y: y Position des Pixels
        :param r: rote Farbe des Pixels
        :param g: gruene Farbe des Pixels
        :param b: blaue Farbe des Pixels
        """
        uni.set_rotation(rotation)
        uni.set_pixel(x, y, r, g, b)

    @staticmethod
    def showText(text, ro, gr, bl, fontSize, speed, minimum, rotation = 90):
        width, height = uni.get_shape()
        colour = (ro, gr, bl)
        font_file = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
        font_size = fontSize
        font = ImageFont.truetype(font_file, font_size)
        w, h = font.getsize(text)

        textX, textY = width, 0
        textWidth, textHeight = width, 0

        textWidth += w + width
        textHeight = max(textHeight, h, 16)

        image = Image.new('RGB', (textWidth, textHeight), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((textX, textY), text, colour, font=font)
        uni.set_rotation(rotation)
        for scroll in range(textWidth - width):
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x + scroll, y))
                    r, g, b = [int(n) for n in pixel]
                    if (r + g + b > minimum) or (r + g + b == 0):
                        uni.set_pixel(width - 1 - x, y, r, g, b)
            uni.show()
            time.sleep(speed)
        uni.off()

    @staticmethod
    def show(rotation = 90):
        uni.set_rotation(rotation)
        uni.show()

