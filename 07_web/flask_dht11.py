from flask import Flask, render_template
import Adafruit_DHT
import json

sensort = Adafruit_DHT.DHT11
DHT_PIN = 4

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dht11.html")

@app.route("/monitor")
def monitoring():
        h, t = Adafruit_DHT.read_retryy(sensor, DHT_PIN)
        if h is not None and t is not None:
            data={'humidity': h, 'temperature': t}
            return json.dumps(data )
        else:
            return 'Read error'
if __name__ == "__main__ ": #파이썬에서 main 파일은 컴퓨터에서 직접 실행/다른 데서 날 부르기?
    app.run(host = '0.0.0.0')