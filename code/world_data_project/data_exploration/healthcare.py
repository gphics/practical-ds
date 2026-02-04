#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:06:56 2026

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

Healthcare & Well-being: Analyze the impact of healthcare metrics (Infant mortality, Fertility Rate, Maternal mortality ratio, Physicians per thousand, Out of pocket health expenditure,) on overall life expectancy across different regions.

"""

target_cols = ["Infant mortality", "Fertility Rate", "Maternal mortality ratio",
               "Physicians per thousand", "Out of pocket health expenditure", "Life expectancy"]


target_df = import_df(target_cols)

sns.heatmap(target_df.corr(), annot=True)

plt.title("Relationship Between Healthcare Metrics & Life Expectancy")

export_fig("healthcare_metrics_vs_life_exp.png")


# showing the relationship scatterplots
# _, ax = plt.subplots(1, 2)

# sns.scatterplot(target_df, x=target_cols[-1], y=target_cols[0], ax=ax[0])

# sns.scatterplot(target_df, x=target_cols[-1], y=target_cols[3], ax=ax[1])

# plt.tight_layout(rect=(0.03, 0.03, 0.95, 0.95))
# plt.suptitle(
#     "Relationship between life expectancy and healthcare metrics".title(), size=10)

# export_fig("healthcare_metrics_vs_life_exp_scatterplot.png")
