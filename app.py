import base64
import io
import os
import requests
import cv2
import pathlib
import matplotlib.pyplot as plt
from flask import Flask, Response, redirect, render_template
from flask import request, flash, url_for, send_from_directory
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from werkzeug.utils import secure_filename

from ImageSegmentation import main, reader

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


app.config['template_path'] = r'\templates'

# check logs
# and try harder for getting it completed tomorrow


def image_return():
    global name
    if request.method == 'POST':
        if request.files:
            print('address accessed')
            file = request.files['img']
            try:
                k = request.values['k']
            except Exception as e:
                pass
            print('DONE FILE')
            if not file.filename == '':
                print('FILENAME EXISTS')
                name = secure_filename(file.filename)
                name = name.split('.')[0]
                address = os.path.join(
                    app.config['template_path'], 'uploads', name)
                print(os.path.join(*(address.split('\\')[1:])))
                address = os.path.join(*(address.split('\\')[1:]))
                print(address)
                print(os.path.splitext(address)[0])
                address = os.path.splitext(address)[0]
                file.save(address)
                print('DONEEEE')
                img = reader(address)

                print(address)
                if k:
                    red_image, path = main(img, name, k)
                else:
                    red_image, path = main(img, name)
                print(f'image red. and saved to path : {path}')

                return red_image, path
            else:
                redirect(request.url)
                return flash('something went wrong try again')
        else:
            redirect(request.url)
            return flash('something went wrong try again')
    else:
        redirect(request.url)
        return flash('something went wrong try again')


    # idhar ek loop aaega jisme ham
    # saare images ka display banaege
'''
it would have been much easier if 
i just let user decide for K's and
just save the image and display it 
why am i going sooo FANCY !!!!
'''


@ app.route('/transformed', methods=['POST', 'GET'])
def transform():
    red_image, path = image_return()

    return render_template('imagetrans.html', address=path)


# @app.route('/templates/static/transformed/<filename>')
# def send_file(filename):
#     return send_from_directory(filename=name)


if __name__ == '__main__':
    app.run(debug=True)
