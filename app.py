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
        img = request.files['img']
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
        # displaying live images from medium article help
        # saving the images in a db


# Matplotlib page
@app.route('/matplot', methods=("POST", "GET"))
def mpl():
    return render_template('imagetrans.html',
                           PageTitle="Matplotlib")


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor('#E8E5DA')

    x = ECS_data.team
    y = ECS_data.gw1

    ax.bar(x, y, color="#304C89")

    plt.xticks(rotation=30, size=5)
    plt.ylabel("Expected Clean Sheets", size=5)

    return fig


if __name__ == '__main__':
    app.run(debug=True)
