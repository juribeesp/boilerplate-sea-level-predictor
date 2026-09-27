import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Create first line of best fit
    res = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    x_pred = pd.Series(range(1880, 2051))

    plt.plot(
        x_pred,
        res.intercept + res.slope * x_pred
    )

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    x_pred_recent = pd.Series(range(2000, 2051))

    plt.plot(
        x_pred_recent,
        res_recent.intercept + res_recent.slope * x_pred_recent
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()