import cv2
from PIL import Image
from flask import Flask, request
from coin.coin_identification import *
from coin.coin_detection import * 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route("/count_coins/", methods = ['POST'])
def count_coins():
    #image = np.fromstring(request.data,np.uint8)
    #coins = get_coins(image)
    #data = dict(request.form)
    #getting data associated with the name file from form
    img = Image.open(request.files['file'])
    #shows pillow jpeg image we send in our http request
    #img.show()
    test = "test.jpg"
    img.save(test)
    #gets file path from saved image
    img_src = os.getcwd()+"/"+test
    # circles is a list (x y coordinates of center and radius) and 
    #image is an image with the circles drawn on it
    circles,image = detect_coin_circles(img_src)
    
    #returns the total value
    calculatedVal = coinFinder(circles)
    
    
    #send_file(cv2.imwrite("test2.jpg", image))
    return str(calculatedVal)




