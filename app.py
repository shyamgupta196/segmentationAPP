from flask import Flask, request, render_template
from ImageSegmentationEdureka import reader, main
import matplotlib.pyplot as plt
import os
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from flask import Response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/images', methods=['POST'])
def trans():
    if request.method == 'POST':
        img = request.files['img']
        filename = secure_filename(img.filename)
        filepath = os.path.join('templates/uploads/',
                                filename)
        title = request.values['title']

        # print(title)
        plt.savefig(filepath)
        img = reader(filepath)

        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)

        grid = main(img, title)
        FigureCanvas(fig).print_png(grid)
        # connecting main with submit
        return render_template('imagetrans.html', grid=grid)


if __name__ == '__main__':
    app.run(debug=True)
