from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return '<h1>考研倒计时:166天</h1><img src="http://helloflask.com/totoro.gif"><h1>考研加油%s</h1>' % name
