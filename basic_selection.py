from machine import Pin, Timer
import time
led = Pin(25, Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

# NOTE: These do not line up with the schematic!
# Ex:
#   SW1 is actually button4
#   SW4 is actually button1
button1 = Pin(28, Pin.IN)
button2 = Pin(27, Pin.IN)
button3 = Pin(26, Pin.IN)
button4 = Pin(22, Pin.IN)

gpioSelU1 = Pin(19, Pin.OUT)
gpioSelU2 = Pin(17, Pin.OUT)
gpioOeU1 = Pin(18, Pin.OUT)
gpioOeU2 = Pin(16, Pin.OUT)

prevButton1 = False
prevButton2 = False
prevButton3 = False
prevButton4 = False

BUTTON_PUSHED = 0
BUTTON_RELEASED = 1
OUTPUT_ENABLED = 0
OUTPUT_DISABLED = 1
SELECT_CHAN_1 = 0
SELECT_CHAN_2 = 1

def selectVGA(num):
    if(num == 1):
        print("Select VGA 1")
        gpioOeU1.value(OUTPUT_ENABLED)
        gpioOeU2.value(OUTPUT_DISABLED)
        gpioSelU1.value(SELECT_CHAN_1)
        # Don't care: gpioSelU2
    elif(num == 2):
        print("Select VGA 2")
        gpioOeU1.value(OUTPUT_ENABLED)
        gpioOeU2.value(OUTPUT_DISABLED)
        gpioSelU1.value(SELECT_CHAN_2)
        # Don't care: gpioSelU2
    elif(num==3):
        print("Select VGA 3")
        gpioOeU1.value(OUTPUT_DISABLED)
        gpioOeU2.value(OUTPUT_ENABLED)
        # Don't care: gpioSelU1
        gpioSelU2.value(SELECT_CHAN_1)

    else:
        print("Select VGA 4")
        gpioOeU1.value(OUTPUT_DISABLED)
        gpioOeU2.value(OUTPUT_ENABLED)
        # Don't care: gpioSelU1
        gpioSelU2.value(SELECT_CHAN_2)



while(True):
    if(prevButton1 != button1.value()):
        prevButton1 = button1.value()
        if(prevButton1 == BUTTON_PUSHED):
            print("Button1 pushed")
            selectVGA(1)
    if(prevButton2 != button2.value()):
        prevButton2 = button2.value()
        if(prevButton2 == BUTTON_PUSHED):
            print("Button2 pushed")
            selectVGA(2)
    if(prevButton3 != button3.value()):
        prevButton3 = button3.value()
        if(prevButton3 == BUTTON_PUSHED):
            print("Button3 pushed")
            selectVGA(3)
    if(prevButton4 != button4.value()):
        prevButton4 = button4.value()
        if(prevButton4 == BUTTON_PUSHED):
            print("Button4 pushed")
            selectVGA(4)
