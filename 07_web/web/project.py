from flask import Flask, render_template
import cv2

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html" , title = "Main")
@app.route("/first")
def first():
    return render_template("execute.html", title = "execute")
@app.route("/help")
def second():
    return render_template("help.html", title = "Second Page")

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    app.run(host="0.0.0.0")