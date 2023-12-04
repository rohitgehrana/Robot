import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the relay
motor_pin = 'WRITE YOUR ACTUAL GPIO PIN'

# Setup the GPIO pin as an output
GPIO.setup(motor_pin, GPIO.OUT)

def start_motor():
    # Turn on the relay to start the motor
    GPIO.output(motor_pin, GPIO.HIGH)
    print("Motor started")

def stop_motor():
    # Turn off the relay to stop the motor
    GPIO.output(motor_pin, GPIO.LOW)
    print("Motor stopped")

try:
    # Start the motor
    start_motor()

    # Wait for 5 seconds (you can adjust this time)
    time.sleep(5)

    # Stop the motor
    stop_motor()

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    stop_motor()
    GPIO.cleanup()  # Cleanup GPIO settings on program exit
