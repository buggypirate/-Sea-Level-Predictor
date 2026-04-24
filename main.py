from sea_level_predictor import draw_plot
import unittest
from test_module import SeaLevelPlotTestCase

draw_plot()

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(SeaLevelPlotTestCase))
runner = unittest.TextTestRunner()
runner.run(suite)
