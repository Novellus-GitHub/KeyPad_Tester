# https://www.digikey.com/en/maker/blogs/2021/how-to-connect-a-keypad-to-a-raspberry-pi

# 3C x 4R Keypad:
# https://www.adafruit.com/product/419

# import required libraries
import RPi.GPIO as GPIO
import time

delay = .50
sLastPressed = str("N")

# The following GPIO pins are connected to the keypad
# Change these according to your connections!

# This code structured for 3 Columns by 4 Rows.
# Rows - GPIO: 23,24,25,26
# Columns - GPIO: 20,21,22

# Rows
L1 = 23
L2 = 24
L3 = 25
L4 = 26

# Columns
C1 = 20
C2 = 21
C3 = 22
# C4 = ??

# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Initialize the GPIO pins for the LEDs - Use BCM GPIO Numbers

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # STAR - Set GPIO 7 (pin #26) to be an output pin and set initial value to low (off)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) # 0 - Set GPIO 4 (pin #7) to be an output pin and set initial value to low (off)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # POUND - Set GPIO 8 (pin #24) to be an output pin and set initial value to low (off)

GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # 1 - Set GPIO 5 (pin #29) to be an output pin and set initial value to low (off)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # 2 - Set GPIO 6 (pin #31) to be an output pin and set initial value to low (off)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # 3 - Set GPIO 12 (pin #32) to be an output pin and set initial value to low (off)

GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # 4 - Set GPIO 13 (pin #33) to be an output pin and set initial value to low (off)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # 5 - Set GPIO 16 (pin #36) to be an output pin and set initial value to low (off)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # 6 - Set GPIO 17 (pin #11) to be an output pin and set initial value to low (off)

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # 8 - Set GPIO 18 (pin #12) to be an output pin and set initial value to low (off)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # 8 - Set GPIO 19 (pin #35) to be an output pin and set initial value to low (off)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) # 9 - Set GPIO 27 (pin #13) to be an output pin and set initial value to low (off)

# Finish initializing the GPIO pins for the LEDs

# Initialize the GPIO pins for the LEDs

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)

# ========  Column #1 - 1, 4, 7, *
    
    if(GPIO.input(C1) == 1):
      print('C1 - Characters[0] equals: ' + characters[0] + '.')
      if (characters[0] == "1"):
        GPIO.output(5, GPIO.HIGH) # 1 - Turn LED 1 ON - Pin #29
        time.sleep(delay)
        last_pressed = (characters[0])
        GPIO.output(5, GPIO.LOW) # 1 - Turn LED 1 OFF - Pin # 29
      elif (characters[0] == "4"):
        GPIO.output(13, GPIO.HIGH) # 4 - Turn LED 4 ON - Pin # 33
        time.sleep(delay)
        GPIO.output(13, GPIO.LOW) # 4 - Turn LED 4 OFF - Pin # 33
      elif (characters[0] == "7"):
        GPIO.output(18, GPIO.HIGH) # 7 - Turn LED 7 ON - Pin # 12
        time.sleep(delay)
        GPIO.output(18, GPIO.LOW) # 7 - Turn LED 7 OFF - Pin # 12
      elif (characters[0] == "*"):
        GPIO.output(7, GPIO.HIGH) # * - Turn LED * ON - Pin # 26
        time.sleep(delay)
        GPIO.output(7, GPIO.LOW) # * - Turn LED * OFF - Pin # 26
        
      sLastPressed = (characters[0]); # Ovewrite the Last Key Pressed Value in variable with newest value from "C0".
      print ('Last Key Pressed: ', sLastPressed) # Print the value of the last key pressed.
     
# ========  Column #2 - 2, 5, 8, 0

    if(GPIO.input(C2) == 1):
     print('C2 - Characters[1] equals: ' + characters[1] + '.')
     if (characters[1] == "2"):
        GPIO.output(6, GPIO.HIGH) # 2 - Turn LED 2 ON - Pin #31
        time.sleep(delay)
        GPIO.output(6, GPIO.LOW) # 2 - Turn LED 2 OFF - Pin # 31
     elif (characters[1] == "5"):
        GPIO.output(16, GPIO.HIGH) # 5 - Turn LED 5 ON - Pin # 36
        time.sleep(delay)
        GPIO.output(16, GPIO.LOW) # 5 - Turn LED 5 OFF - Pin # 36
     elif (characters[1] == "8"):
        GPIO.output(19, GPIO.HIGH) # 8 - Turn LED 8 ON - Pin # 35
        time.sleep(delay)
        GPIO.output(19, GPIO.LOW) # 8 - Turn LED 8 OFF - Pin # 35
     elif (characters[1] == "0"):
        GPIO.output(4, GPIO.HIGH) # 0 - Turn LED 0 ON - Pin # 7
        time.sleep(delay)
        GPIO.output(4, GPIO.LOW) # 0 - Turn LED 0 OFF - Pin # 7
        
     sLastPressed = (characters[1]); # Ovewrite the Last Key Pressed Value in variable with newest value from "C1".
     print ('Last Key Pressed: ', sLastPressed) # Print the value of the last key pressed.

# ========  Column #3 - 3, 6, 9, #

    if(GPIO.input(C3) == 1):
     print('C3 - Characters[2] equals: ' + characters[2] + '.')
     if (characters[2] == "3"):
        GPIO.output(12, GPIO.HIGH) # 3 - Turn LED 3 ON - Pin #32
        time.sleep(delay)
        GPIO.output(12, GPIO.LOW) # 3 - Turn LED 3 OFF - Pin # 32
     elif (characters[2] == "6"):
        GPIO.output(17, GPIO.HIGH) # 6 - Turn LED 6 ON - Pin # 11
        time.sleep(delay)
        GPIO.output(17, GPIO.LOW) # 6 - Turn LED 6 OFF - Pin # 11
     elif (characters[2] == "9"):
        GPIO.output(27, GPIO.HIGH) # 9 - Turn LED 9 ON - Pin # 13
        time.sleep(delay)
        GPIO.output(27, GPIO.LOW) # 9 - Turn LED 9 OFF - Pin # 13
     elif (characters[2] == "#"):
        GPIO.output(8, GPIO.HIGH) # # - Turn LED # ON - Pin # 24
        time.sleep(delay)
        GPIO.output(8, GPIO.LOW) # # - Turn LED # OFF - Pin # 24

     sLastPressed = (characters[2]); # Ovewrite the Last Key Pressed Value in variable with newest value from "C2".
     print ('Last Key Pressed: ', sLastPressed) # Print the value of the last key pressed.


# ========  Column #4

#    if(GPIO.input(C4) == 1):
#        print(characters[3])

    GPIO.output(line, GPIO.LOW)
 


try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["1","2","3"])
        readLine(L2, ["4","5","6"])
        readLine(L3, ["7","8","9"])
        readLine(L4, ["*","0","#"])
        time.sleep(0.25)
        
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
