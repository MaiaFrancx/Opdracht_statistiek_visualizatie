
# Libraries
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.distributions.empirical_distribution import ECDF

# Constants
dirdataprod = os.path.join(os.path.dirname(os.getcwd()), "Data\Input\Data_productie")
dirbru = os.path.join(os.path.dirname(os.getcwd()), "Data\Input\Data_productie\Daily_production\BRU")
dirsto = os.path.join(os.path.dirname(os.getcwd()), "Data\Input\Data_productie\Daily_production\STO")

# Functions


def df_from_json_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        with open(full_path) as file_object:
            data = json.load(file_object)
        data_list.append(data)
    df = pd.DataFrame(data_list)
    return df


def df_clean(df):
    df_cleaned = df.copy()
    columns_to_drop = [col for col in ['hour', 'minute'] if col in df_cleaned.columns]
    df_cleaned.drop(columns_to_drop, axis=1, inplace=True)
    df_cleaned.replace('#MV', np.NaN, inplace=True)
    df_cleaned.fillna(0, inplace=True)
    df_cleaned["prod_loss"] = df_cleaned["prod_loss"].astype(int)
    df_cleaned["prod_loss_perc"] = df_cleaned["prod_loss_perc"].astype(int)
    df_cleaned["production"] = df_cleaned["production"].astype(int)
    df_cleaned["date"] = pd.to_datetime(df_cleaned["date"]).dt.date
    df_cleaned["date"] = df_cleaned["date"].astype('datetime64[ns]')
    return df_cleaned


def plot_production(df, ax, title, hline):
    """Plot production data on given axes with specific configuration."""
    df.plot(x="date", y="production", ax=ax, legend=False)
    ax.axhline(hline, color='r')
    ax.set_title(title + ' Production')
    ax.set_xlabel('Date')
    ax.set_ylabel('Production')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def plot_histogram(df, column, axp, title='', binsp=50, alphap=0.5, colorp='b', densityp=False):
    """
    Plots a histogram for a specified column of a DataFrame.

    Parameters:
    - df: DataFrame containing the data.
    - column: String, the name of the column to plot.
    - ax: matplotlib axis object on which to plot the histogram.
    - title: String, title of the histogram.
    - bins: Integer, number of bins to use in the histogram.
    """
    df.hist(column, bins=binsp, ax=axp, alpha=alphap, color=colorp, density=densityp)
    axp.set_title(title)
    axp.set_xlabel(column)
    axp.set_ylabel('Frequency')
    axp.spines['top'].set_visible(False)
    axp.spines['right'].set_visible(False)


def model_prod(p, mu, sigma):
    """
    Function calculates the production for one day
    The chance of having zere production is p
    So there's a (1 - p) chance that there is production
    The mu parameter is the mean value
    The sigma parameter is the standard deviation
    """

    a = np.random.rand()
    if a < p:
        return 0
    else:
        return np.random.normal(loc=mu, scale=sigma)

def plot_ecdf(ecdf, ax, title='ECDF'):
    """
        Plots an ECDF on a specified axes object.

        Parameters:
        - ecdf: ECDF object (must have .x and .y attributes).
        - ax: matplotlib axes object where the ECDF will be plotted.
        - title: Title for the plot.
        """
    ax.plot(ecdf.x, ecdf.y)
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('ECDF')
    axp.spines['top'].set_visible(False)
    axp.spines['right'].set_visible(False)
    ax.grid(True)
