from flask import Flask, request, render_template
from ImageSegmentationEdureka import reader, main
import matplotlib.pyplot as plt
import os
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
from flask import Response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/images', methods=['POST'])
def trans():
    if request.method == 'POST':
        img = request.image['img']
        filename = secure_filename(img.filename)
        filepath = os.path.join('templates/uploads/',
                                filename)
        title = request.values['title']
        # print(title)
        plt.savefig(filepath)
        img = reader(filepath)

        fig = Figure()
        # axis = fig.add_subplot(1, 1, 1)
        main(img, title)
        output = io.BytesIO()
        fig.savefig(output, format='png')
        # Embed the result in the html output.
        data = base64.b64encode(output.getbuffer()).decode("ascii")
        # canvas = FigureCanvas(fig).print_png(grid)
        return f"<img src='data:image/png;base64,{data}'/>"
        # connecting main with submit?????


if __name__ == '__main__':
    app.run(debug=True)
