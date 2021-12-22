import RPi.GPIO as GPIO
import time


LED_PIN = 16
LED_PIN_1 = 12
LED_PIN_2 = 21

SWITCH_PIN_1 = 13
SWITCH_PIN_2 = 19
SWITCH_PIN_3 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

GPIO.setup(SWITCH_PIN_1, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_2, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_3, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)


try:
    while True:
        val = GPIO.input(SWITCH_PIN_1)
        print(val)
        GPIO.output(LED_PIN, val)
        val = GPIO.input(SWITCH_PIN_2)
        print(val)
        GPIO.output(LED_PIN_1, val)
        val = GPIO.input(SWITCH_PIN_3)
        print(val)
        GPIO.output(LED_PIN_2, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')




