import RPi.GPIO as GPIO
import time

BUZZER_PIN = 21 
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#주파수 설정(262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) #duty cycle(0~100) -소리 크기 조절

melody = [392,392,440,440,392,392,330,392,392,330,330,294,392,392,440,440,392,392,330,392,330,294,330,262]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)


finally:
    pwm.stop()
    GPIO.cleanup()