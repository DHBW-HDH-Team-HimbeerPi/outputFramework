# outputFramework

For Install
```pip3 install https://github.com/DHBW-HDH-Team-HimbeerPi/outputFramework/releases/download/latest/output_framework_simon_berndt-0.0.1-py3-none-any.whl```


All the Methods

```
setWindow()
setPixel()
showText()
show()
```


SetWindow()

```
list (16x16x3)
rotation (optional; normal 90 degree)
```


setPixel()

```
x: int (0-15)
y: int (0-15)
r: int (0-255)
g: int (0-255)
b: int (0-255)
rotation (optional; normal 90 degree)

TO SHOW THE SETTED PIXELS; YOU HAVE TO CALL "show()"
```


showText()

```
USED FOR SCROLLING A STRING

text: string
ro: int (0-255)
gr: int (0-255)
bl: int (0-255)
fontsize: int (good size for readable text is 12)
speed: (time in seconds; time for waiting to next step in scrolling; good speed is between 0.05 - 0.1)
minimum: (if higher there are only full pixel generated, but the best is just 0)
rotation (optional; normal 90 degree)
```


show()

```
shows all setted pixels.

rotation: int (optional; normal 90 degree)
```
