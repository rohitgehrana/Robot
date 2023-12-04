#First install this package "pip install rpi_ws281x adafruit-circuitpython-neopixel"




import board
import neopixel
import time

# Define the GPIO pin connected to the LED matrix
led_pin = board.D18  # Assuming GPIO 37 is pin 18 on the Raspberry Pi

# Define the number of LEDs in the matrix
num_leds = 64

# Create a NeoPixel object
pixels = neopixel.NeoPixel(led_pin, num_leds, auto_write=False)

def set_led_color(index, color):
    # Set the color of the specified LED
    pixels[index] = color
    pixels.show()

def turn_off_leds():
    # Turn off all LEDs in the matrix
    pixels.fill((0, 0, 0))
    pixels.show()

def rainbow_cycle(wait_time):
    # Display a rainbow cycle on the LED matrix
    for j in range(255):
        for i in range(num_leds):
            pixel_index = (i * 256 // num_leds) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait_time)

def wheel(pos):
    # Generate rainbow colors
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

try:
    # Example: Display a rainbow cycle on the LED matrix
    rainbow_cycle(0.05)

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    turn_off_leds()
