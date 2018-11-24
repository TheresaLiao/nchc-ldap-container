#!/usr/bin/env python
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.inception_v3 import *
from tensorflow.python.keras import backend as K

import numpy as np
import os
import json

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def InceptV3(img):
    # Load InceptionV3 Image
    model = InceptionV3(include_top=True, weights='imagenet')
    # Resize the image
    img = image.load_img(img, target_size=(299, 299))
    # Change the image to array
    x = image.img_to_array(img)
    # Add dimension to image
    x = np.expand_dims(x, axis=0)
    # Normalize the data between 0 to 1
    x = preprocess_input(x)
    # Get prediciton
    preds = model.predict(x)
    K.clear_session()
    result = dict((key, str(value)) for (_,key, value) in decode_predictions(preds)[0])
    return json.dumps(result)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            predict_results = InceptV3(img)
            return predict_results
    return  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
