from bottle import *

# 一番最初はここが実行される
@route("/")
def index():
    return template("index")

run(host='localhost', port=8080, reloader=True)
