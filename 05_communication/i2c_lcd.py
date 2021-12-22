from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 19

now = datetime.datetime.now()

display = drivers.Lcd()

try:
    print('Writing to Display')
    display.lcd_display_string(now.strftime("%x %X") , 1)
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string('%.1f*C, %.1f%%' % (t, h), 2)
        time.sleep(0.5)

finally:
    print('cleaning up')
    display.lcd_clear()