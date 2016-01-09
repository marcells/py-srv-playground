from flask import Flask
import os
app = Flask(__name__)
hits = 0

@app.route('/')
def hello():
    global hits
    hits += 1
    
    return 'Hello World! I have been seen %s times.' % hits

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
