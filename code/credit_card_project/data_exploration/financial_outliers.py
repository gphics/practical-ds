#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:22:02 2026

@author: xenon
"""
import sys
from pathlib import Path
from data_entry import get_df_info, export_fig, import_df
import matplotlib.pyplot as plt


parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)


# Task:
"""
Financial Outliers
1. Transaction Magnitude: How do individual transaction amounts compare to the user’s overall mean spending?

2. High-Volume Merchants: Which specific merchants or categories are responsible for the most "outlier" (extreme value) transactions?

"""

target_cols = ["amt", "merchant", "category"]
target_df = import_df(target_cols)

# 1.
trans_magnitude = target_df[target_cols[0]].describe()
trans_magnitude = trans_magnitude.apply(lambda x: format(x, 'f'))


# 2.
# getting the quantiles
q1, q3 = target_df[target_cols[0]].quantile([0.25, 0.75])

# calculating the iqr
iqr = q3 - q1

# getting the lower and upper limit of the feature(amt)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5*iqr

# selecting outliers
outlier_conditions = (target_df[target_cols[0]] <
                      lower_bound) | (target_df[target_cols[0]] > upper_bound)

outliers_df = target_df[outlier_conditions]

# subsetting base on specific features
merchant_group = target_df.groupby(target_cols[1])[
    target_cols[0]] .sum().sort_values(ascending=False)
category_group = target_df.groupby(
    target_cols[-1])[target_cols[0]] .sum().sort_values(ascending=False)


# plotting groups
_, ax = plt.subplots(1, 2)

# plotting the graphs
merchant_group[:5].plot(kind="bar", ax=ax[0])
category_group[:5].plot(kind="bar", ax=ax[1])

# ax0 plot styles
ax[0].tick_params(axis="both", labelsize=7)
ax[0].set_ylabel("Amount($)", size=8)
ax[0].set_xlabel("Merchant", size=8)

# ax1 plot styles
ax[1].tick_params(axis="both", labelsize=7)
ax[1].set_ylabel("Amount($)", size=8)
ax[1].set_xlabel("Category", size=8)

# general plot styles
plt.tight_layout(rect=(0.03, 0.03, 0.95, 0.95))
plt.suptitle("Outliers Bar PLot", size=10)


# saving fig
# export_fig("outliers_bar_plot.png")
