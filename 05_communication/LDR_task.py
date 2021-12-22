import spidev
import time
import RPi.GPIO as GPIO
import time
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
spi = spidev.SpiDev()

spi.open(0,0) # bus: 0, dev: 0

spi.max_speed_hz = 100000


def analog_read(channel):
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out


try:
    while True:
        reading = analog_read(0)
        print("Reading=%d" % reading)
        time.sleep(0.5)
        GPIO.output(LED_PIN, 0 if reading>=512 else 1)
                

finally:
    spi.close()
    GPIO.cleanup()  