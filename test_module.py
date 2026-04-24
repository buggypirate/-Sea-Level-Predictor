import unittest
import pandas as pd
from scipy.stats import linregress
import sea_level_predictor
import matplotlib as mpl
mpl.use('Agg')


class SeaLevelPlotTestCase(unittest.TestCase):

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), 'Rise in Sea Level')

    def test_plot_xlabel(self):
        self.assertEqual(self.ax.get_xlabel(), 'Year')

    def test_plot_ylabel(self):
        self.assertEqual(self.ax.get_ylabel(), 'Sea Level (inches)')

    def test_plot_data_points(self):
        scatter = self.ax.collections[0]
        df = pd.read_csv('epa-sea-level.csv')
        self.assertEqual(len(scatter.get_offsets()), len(df))

    def test_line1_points(self):
        # First line of best fit should end at 2050
        lines = self.ax.lines
        self.assertTrue(any(line.get_xdata()[-1] == 2050 for line in lines))

    def test_line2_points(self):
        # Second line (from 2000) should also end at 2050
        lines = self.ax.lines
        self.assertTrue(any(line.get_xdata()[0] >= 2000 and line.get_xdata()[-1] == 2050 for line in lines))


if __name__ == '__main__':
    unittest.main()
