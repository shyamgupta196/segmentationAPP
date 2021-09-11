from flask import Flask, request, render_template, redirect
from ImageSegmentationEdureka import reader, main
import matplotlib.pyplot as plt
import os
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
import cv2
from flask import Response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


app.config['template_path'] = r'C:\Users\Asus\Documents\deep learning\deep_learn\NOTEBOOKS\app\templates'

# check logs
# and try harder for getting it completed tomorrow


def image_return():
    if request.method == 'POST':
        if request.files:
            print('address accessed')
            file = request.files['img']
            print('DONE FILE')
            if not file.filename == '':
                print('FILENAME EXISTS')
                name = secure_filename(file.filename)
                print(name)
                address = os.path.join(
                    app.config['template_path'], 'uploads/', name)
                file.save(address)
    print('DONEEEE')
    img = reader(address)
    image = main(img)
    segmented_img = os.path.join(
        app.config['template_path'], 'transformed/', name)
    cv2.imwrite(segmented_img, image)
    print('IMAGE IS SAVED IN TRANSFORMED')
    return image, segmented_img


@ app.route('/transformed', methods=['POST'])
def transform():
    image, address = image_return()
    return render_template('imagetrans.html', address=address)


if __name__ == '__main__':
    app.run(debug=True)
