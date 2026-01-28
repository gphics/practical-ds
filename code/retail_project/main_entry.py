#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:44:36 2026

@author: xenon

@description: This file is the one that read the processed data from the data dir and make it available for other files for consumption.

"""
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

file_path = base_dir / ".." / "data" / "cleaned_online_retail.csv"


df = pd.read_csv(file_path, parse_dates=[
    "InvoiceDate"])


def export_df():
    """
    This function helps to export a full cloned version of the dataframe, to prevent unexpected or unintended mutation of the original dataframe
    """
    new_df = df.copy()
    return new_df


sns.set_theme(style="white", palette="husl")


def export_fig(fig_name):

    try:
        fig_path = str(base_dir) + \
            "/retail_project/visuals/{}".format(fig_name)
        plt.savefig(fig_path)
    except Exception as e:
        print(e)
