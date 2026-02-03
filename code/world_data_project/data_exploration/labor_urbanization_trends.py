#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 16:47:25 2026

@author: xenon
"""
from data_entry import import_df, get_df_info, export_fig
import sys
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

# Task

"""
Labor & Urbanization Trends: Study the dynamics between urban population percentage, labor force participation,Unemployment rate, and minimum wage levels.

"""

get_df_info()
target_cols = ["Urban_population",
               "Population: Labor force participation (%)", "Unemployment rate", "Minimum wage"]

target_df = import_df(target_cols)

corr_df = target_df.corr()

sns.heatmap(corr_df, annot=True)


plt.title("Labor & Urbanization Trends")
export_fig("labor_&_urbanization_trends.png")
