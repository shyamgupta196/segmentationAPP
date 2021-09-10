from flask import Flask, request, render_template, redirect
from ImageSegmentationEdureka import reader, main
import matplotlib.pyplot as plt
import os
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
from PIL.Image import Image
from flask import Response

app = Flask(__name__)

# request.url = '/'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/showingimage')
def show():
    return render_template('imagetrans.html')


@app.route('/transformed.png', methods=['POST'])
def transform():
    print('DONEEEE')
    filename = address()
    img = reader(filename)
    image = main(img)
    Image.save(image, os.path.join('/templates/transformed/', filename))
    print('IMAGE IS SAVED IN TRANSFORMED')
    return image


def address():
    print('address accessed')
    if request.method == 'POST':
        if request.files:
            file = request.files['img']
            print('DONE FILE')
            if not file.filename == '':
                print('FILENAME EXISTS')
                name = secure_filename(file.filename)
                address = os.path.join('/templates/uploads/', name)
                file.save(address)
                print('IMAGE IS SAVED')
    return address


if __name__ == '__main__':
    app.run(debug=True)
