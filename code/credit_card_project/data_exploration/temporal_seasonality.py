#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:11:06 2026

@author: xenon
"""

import sys
from pathlib import Path
from data_entry import get_df_info, export_fig, import_df
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pointbiserialr, mannwhitneyu

parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

# Task:
"""
Temporal Seasonality

1. Day-of-Week Analysis: Does spending volume significantly increase on weekends compared to weekdays?

2. Monthly Cycles: Are there visible "payday" spikes in the data where transaction volume surges at the beginning or end of the month?

"""

target_cols = ["day_name", "month_day", "month", "year", "is_weekend", "amt"]
target_df = import_df(target_cols)


# 1.
spending_vol_group = target_df.groupby(target_cols[-2])["amt"]
spending_vol_sum = spending_vol_group.sum()
spending_vol_stat = spending_vol_group.describe()

pb = pointbiserialr(target_df[target_cols[-2]], target_df[target_cols[-1]])

# subseting df base on is_weekend
condition = target_df[target_cols[-2]] == True
weekend_df = target_df[condition]["amt"]
weekday_df = target_df[~condition]["amt"]


mann = mannwhitneyu(weekend_df, weekday_df, alternative="less")


# # plotting graph
# ax = spending_vol_sum.plot(kind="bar")

# # styling graph
# ax.ticklabel_format(style="plain", axis="y")
# ax.set_ylabel("Amount($)")
# plt.title("Spending Amount")

# # exporting fig
# export_fig("spending_amount.png")


# 2.
spikes = target_df.groupby(target_cols[1])["amt"]

sum_spikes = spikes.sum()
freq_spikes = spikes.size()

# # Graph Plotting
# _, ax = plt.subplots(1, 2, gridspec_kw={
#                      "width_ratios": [2, 1]}, figsize=(13, 6))

# sum_spikes.plot(kind="bar",  ax=ax[0])
# freq_spikes.plot(ax=ax[1])

# # general fig styles
# plt.tight_layout(rect=[0.03, 0.03, 0.95, 0.95])
# plt.suptitle("Payday spikes", size=10)

# # ax0 style
# ax[0].tick_params(axis="both", labelsize=8)
# ax[0].set_ylabel("Amount($)", size=9)
# ax[0].set_xlabel("Day of Month", size=9)

# # ax1 style
# ax[1].set_xlim(0, 32)
# ax[1].set_ylim(20000, 50000)
# ax[1].tick_params(axis="both", labelsize=8)
# ax[1].set_ylabel("Number of Transaction", size=9)
# ax[1].set_xlabel("Day of Month", size=9)


# # saving plot
# export_fig("transaction_spikes.png")
