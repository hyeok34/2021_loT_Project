import RPi.GPIO as GPIO
import time
LED_PIN = 4
LED_PIN1 = 5
LED_PIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)


GPIO.output(LED_PIN, GPIO.HIGH)
print("led on")
time.sleep(2)
GPIO.output(LED_PIN, GPIO.LOW)
print("led off")

GPIO.output(LED_PIN1, GPIO.HIGH)
print("led on")
time.sleep(2)
GPIO.output(LED_PIN1, GPIO.LOW)
print("led off")

GPIO.output(LED_PIN2, GPIO.HIGH)
print("led on")
time.sleep(2)
GPIO.output(LED_PIN2, GPIO.LOW)
print("led off")




GPIO.cleanup() #초기화





