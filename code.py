# Rasperry Pico Mouse Jiggler Delux
#

import time
import board
import digitalio
import neopixel
import usb_hid
from adafruit_hid.mouse import Mouse



# Set NeoPixel
pixel_pin = board.GP0
num_pixels = 1
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# Set HID Mouse
mouse = Mouse(usb_hid.devices)

#Set onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(5)
led.value = False
time.sleep(5)


pixels.fill((0, 255, 0))
pixels.show()

# Set the number of pixel the mouse will moved
mdelta = 2
# set the time in second between 
mloop = 30
mloopS = int(round(mloop * 0.1))
mloopE = int(round(mloop * 0.9))
print(mloopS)
print(mloopE)

mstart = time.time()
print("Start Loop")

while True:
    mcurrent = time.time()
    if mcurrent >= mstart + mloop:     
        mstart = mcurrent
        print(mcurrent)
        led.value = True
        time.sleep(0.1)
        mouse.move(mdelta * -1, mdelta * -1, 0)
        led.value = False
        mouse.move(mdelta, mdelta, 0)
        print("Mouse move")
        
    if mcurrent-mstart <= mloopS:
        pixels.fill((0, 255, 0))
        pixels.show()
        print("Start Ramp")
        
    elif mcurrent-mstart > mloopS and mcurrent-mstart < mloopE:
        pixels.fill((0, 0, 255))
        pixels.show()
        print("Middle Ramp")
        
    elif mcurrent-mstart >= mloopE:
        pixels.fill((255, 0, 0))
        pixels.show()
        print("End Ramp")
    time.sleep(1)

