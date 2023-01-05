from flask import Flask
from flask import send_file
import os
app = Flask(__name__)             

currDir = "C:/Users/Bhavesh/Desktop/Bhavesh/live-image-project/data-sensing-ss/one.png"

@app.route("/")                   
def hello():                      
    return "Hello World!"

@app.route('/get_image')
def get_image():
    return send_file(currDir)

if __name__ == "__main__":
    app.run()                     