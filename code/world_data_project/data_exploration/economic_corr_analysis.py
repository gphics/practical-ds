#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 10:58:15 2026

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
Economic Correlation Analysis: Investigate the relationship between GDP and socio-economic factors like life expectancy, literacy rates, and unemployment.

"""


target_cols = ["GDP", "Unemployment rate", "Life expectancy",
               "Gross primary education enrollment (%)", "Gross tertiary education enrollment (%)"]

target_df = import_df(target_cols)

# calculating correlation coeficient
corr_df = target_df.corr()

# plotting the correlations
sns.heatmap(corr_df, annot=True)
plt.title("Relationship between GDP & Socio-economic Factors")

# saving figure
export_fig("gdp_corr_socio_eco_factors.png")
