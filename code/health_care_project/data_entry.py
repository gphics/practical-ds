#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 15:52:45 2026

@author: xenon

@description: This module is responsible for reading the data file, engineering out new features from it and making the data (deep clone version) available for other modules

"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


base_dir = Path(__file__).resolve().parent

data_file_path = base_dir / ".." / ".." / "data/healthcare_dataset.csv"

df = pd.read_csv(data_file_path, parse_dates=[
                 "Date of Admission", "Discharge Date"])

# Feature engineering

# creating age group feature
bins = [13, 19, 29, 39, 49, 59, 69, 79, 89]
labels = ["teens", "vicenarians", "thirties", "fourties",
          "fifties", "sixties", "seventies", "eighties"]

df["Age Group"] = pd.cut(df["Age"], bins=bins,
                         labels=labels, include_lowest=True)


# creating the treatment duration feature
df["Admission Duration"] = df["Discharge Date"] - df["Date of Admission"]
df["Admission Duration(INT)"] = df["Admission Duration"].astype(
    str).str.strip(" days").astype(int)


def import_df(cols=[]):
    """
    @description: This function is responsible for copying and importing the dataset.
    @params: 
        cols: An optional parameter containing list of columns to import

    @returns: DF
    """
    new_df = None
    if len(cols):
        new_df = df[cols].copy()
    else:
        new_df = df.copy()
    return new_df


def get_df_info():
    """
    This function is for printing the information about the entire dataset
    """
    print(df.info())


# setting plot styles
sns.set_theme(style="ticks", palette="viridis")


def export_fig(fig_name: str) -> None:
    """
    @params: 
        fig_name: Name to save the figure with

    @description:
        This function is responsible for saving plot figures to the visuals directories

    @returns:
        None
    """

    save_to_path = str(base_dir) + "/visuals/{}".format(fig_name)
    plt.savefig(save_to_path)


get_df_info()
