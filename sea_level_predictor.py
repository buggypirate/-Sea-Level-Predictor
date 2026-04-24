import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Import data from CSV
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data', s=10, color='steelblue')

    # 3. Line of best fit using ALL data (1880 - 2050)
    slope1, intercept1, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(int(df['Year'].min()), 2051))
    ax.plot(years_all, intercept1 + slope1 * years_all, 'r', label='Best Fit Line (all data)')

    # 4. Line of best fit using data from year 2000 onward (2000 - 2050)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = pd.Series(range(2000, 2051))
    ax.plot(years_2000, intercept2 + slope2 * years_2000, 'g', label='Best Fit Line (2000+)')

    # 5. Axis labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return
    plt.savefig('sea_level_plot.png')
    return plt.gca()
