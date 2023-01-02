from flask import Flask
from flask import send_file
app = Flask(__name__)             

@app.route("/")                   
def hello():                      
    return "Hello World!"

@app.route('/get_image')
def get_image():
    return send_file('one.jpeg')

if __name__ == "__main__":
    app.run()                     