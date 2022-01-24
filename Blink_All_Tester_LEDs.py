#! /usr/bin/env python3

# This Python script uses GPIO #4 - For this reason - One-Wire Interface mst NOT be switched to ON in the Pi configuration.
# Having One-Wire endbled in the configuration causes GPIO 4 (Pin #7) to go low and remain there.

# This Python script is a test of all the LEDs that are part of the 4x3 Membrane Keypad Test Interface.
# https://www.adafruit.com/product/419?gclid=CjwKCAiAlrSPBhBaEiwAuLSDUKTfBtUm83XMudyqMLDWThkco6ngumt0EyuotlLpNCtcZlchZ42s3xoCMnAQAvD_BwE

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # STAR - Set GPIO 7 (pin #26) to be an output pin and set initial value to low (off)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # 0 - Set GPIO 4 (pin #7) to be an output pin and set initial value to low (off)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # POUND - Set GPIO 8 (pin #24) to be an output pin and set initial value to low (off)

GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW) # 1 - Set GPIO 5 (pin #29) to be an output pin and set initial value to low (off)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW) # 2 - Set GPIO 6 (pin #31) to be an output pin and set initial value to low (off)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW) # 3 - Set GPIO 12 (pin #32) to be an output pin and set initial value to low (off)

GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW) # 4 - Set GPIO 13 (pin #33) to be an output pin and set initial value to low (off)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) # 5 - Set GPIO 16 (pin #36) to be an output pin and set initial value to low (off)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # 6 - Set GPIO 17 (pin #11) to be an output pin and set initial value to low (off)

GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # 8 - Set GPIO 18 (pin #12) to be an output pin and set initial value to low (off)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW) # 8 - Set GPIO 19 (pin #35) to be an output pin and set initial value to low (off)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # 9 - Set GPIO 27 (pin #13) to be an output pin and set initial value to low (off



while True: # Run forever
 
 print("Switching ON all of the LEDs") # Start the process of switching all of the LEDs to ON
 
 GPIO.output(26, GPIO.HIGH) # Star - Turn on
 GPIO.output(7, GPIO.HIGH) # 0 - Turn on - RPi ONE-WIRE Interface must NOT be enabled.
 GPIO.output(24, GPIO.HIGH) # Pound - Turn on
 
 GPIO.output(29, GPIO.HIGH) # 1 - Turn on
 GPIO.output(31, GPIO.HIGH) # 2 - Turn on
 GPIO.output(32, GPIO.HIGH) # 3 - Turn on
 
 GPIO.output(33, GPIO.HIGH) # 4 - Turn on
 GPIO.output(36, GPIO.HIGH) # 5 - Turn on
 GPIO.output(11, GPIO.HIGH) # 6 - Turn on
 
 GPIO.output(12, GPIO.HIGH) # 7 - Turn on
 GPIO.output(35, GPIO.HIGH) # 8 - Turn on
 GPIO.output(13, GPIO.HIGH) # 9 - Turn on

 print("All LEDs are ON") 
 
 sleep(1) # Sleep for 1 second
 
 print("Switching OFF all of the LEDs") # Start the process of switching all of the LEDs to OFF
 
 GPIO.output(26, GPIO.LOW) # Star - Turn off
 GPIO.output(7, GPIO.LOW) # 0 - Turn off- RPi ONE-WIRE Interface must NOT be enabled.
 GPIO.output(24, GPIO.LOW) # Pound - Turn off
 
 GPIO.output(29, GPIO.LOW) # 1 - Turn off
 GPIO.output(31, GPIO.LOW) # 2 - Turn off 
 GPIO.output(32, GPIO.LOW) # 3 - Turn off
 
 GPIO.output(33, GPIO.LOW) # 4 - Turn off
 GPIO.output(36, GPIO.LOW) # 5 - Turn off
 GPIO.output(11, GPIO.LOW) # 6 - Turn off
 
 GPIO.output(12, GPIO.LOW) # 7 - Turn off
 GPIO.output(35, GPIO.LOW) # 8 - Turn off
 GPIO.output(13, GPIO.LOW) # 9 - Turn off
 
 print("All LEDs are OFF") 
 
 sleep(1) # Sleep for 1 second
