from flask import Flask, send_file
from sea_level_predictor import draw_plot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    draw_plot()
    plt.close()
    return send_file('sea_level_plot.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
