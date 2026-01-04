import machine
import neopixel
import ssd1306
import time

# --- Configuration ---
NUM_LEDS = 4
NEOPIXEL_PIN = 26
OLED_WIDTH = 128
OLED_HEIGHT = 32

# --- Initialize Hardware ---
# Setup NeoPixels
pixels = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), NUM_LEDS)

# Setup I2C for OLED (Pins 6 and 7)
i2c = machine.I2C(1, sda=machine.Pin(6), scl=machine.Pin(7))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

# Setup Buttons (Using internal Pull-Up resistors as they connect to GND)
btn1 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
btn2 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_UP)
btn3 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
btn4 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)


def update_display(text):
    oled.fill(0)  # Clear screen
    oled.text("System Ready", 0, 0)
    oled.text(text, 0, 16)
    oled.show()


def set_leds(color):
    for i in range(NUM_LEDS):
        pixels[i] = color
    pixels.write()


# Initial State
update_display("Press a Button")
set_leds((0, 0, 0))  # Turn off

while True:
    # Check Button 1 - Red
    if not btn1.value():
        update_display("Button 1: RED")
        set_leds((255, 0, 0))

    # Check Button 2 - Green
    elif not btn2.value():
        update_display("Button 2: GREEN")
        set_leds((0, 255, 0))

    # Check Button 3 - Blue
    elif not btn3.value():
        update_display("Button 3: BLUE")
        set_leds((0, 0, 255))

    # Check Button 4 - White
    elif not btn4.value():
        update_display("Button 4: WHITE")
        set_leds((255, 255, 255))

    time.sleep(0.1)  # Small debounce delay