#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:29:58 2026

@author: xenon
"""
from data_entry import import_df, export_fig
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chisquare, mannwhitneyu
import seaborn as sns
import numpy as np
import pingouin as pg
import scikit_posthocs as sp


parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)


# Tasks:
"""
1. Hourly Velocity: At what hour of day do most transactions occur, and do "off-hour" transactions (e.g., 3 AM) show different spending amounts?
2. Category Spending: Which categories (e.g., health_fitness vs. online_retail) have the most frequent transactions versus the highest total monetary value?
"""

target_cols = ["amt", "category", "hour", "off_hour"]
target_df = import_df(target_cols)

# 1
hourly_velocity = target_df.groupby(
    target_cols[2]).size().sort_values(ascending=False)

# plotting ...
# hourly_velocity.plot(kind="bar")
# plt.ylabel("Count")
# plt.xticks(size=8)
# plt.title("Hourly Velocity")
# export_fig("hourly_velocity.png")

# off-hour spending amounts distribution
off_hour_spending = target_df.groupby(target_cols[-1])[target_cols[0]]

sum_stat = off_hour_spending.describe()
# print(sum_stat)
off_hour_spending_sum = off_hour_spending.sum()

# plotting
# _, ax = plt.subplots(1, 2)

# first plot: Sum difference between off-hour and non-off-hour transactions
# off_hour_spending_sum.plot(kind="bar", ax=ax[0])

# setting plot styles
# ax[0].ticklabel_format(style="plain", axis="y")
# ax[0].set_ylabel("Amount($)", size=8)
# ax[0].set_xlabel("Off hour", size=8)
# ax[0].tick_params(axis="both", labelsize=8)

# second plot: Count difference between off-hour and non-off-hour transactions
# sns.countplot(target_df, x=target_cols[-1], ax=ax[1])

# setting plot styles
# ax[1].set_ylabel("Count", size=8)
# ax[1].set_xlabel("Off hour", size=8)
# ax[1].tick_params(axis="both", labelsize=8)

# general plot styles
# plt.suptitle("Amount categorized by off hour".title(), size=10)
# plt.tight_layout()
# export_fig("amount_cat_by_off_hour.png")


# Assosciativity between off-hour freq

#  True False
# The sum equals the total length of the target df
expected_freq = [648337, 648338]
observed_freq = [431216, 865459]

chi_res = chisquare(observed_freq, expected_freq)


# Assosciativity between off-hour using amount spent

amt_sum_stat = target_df[target_cols[0]].describe()

condition = target_df[target_cols[-1]] == True

off_hour_df = target_df[condition][target_cols[0]]
non_off_hour_df = target_df[~condition][target_cols[0]]

mann_res = mannwhitneyu(off_hour_df, non_off_hour_df, alternative="greater")


# 2


category_group = target_df.groupby([target_cols[1]])
cat_freq_size = category_group.size().sort_values(ascending=False)
cat_amnt_sum = category_group[target_cols[0]
                              ].sum().sort_values(ascending=False)


# plotting the barplot
_, ax = plt.subplots(1, 2)
cat_freq_size.plot(kind="bar", ax=ax[0])

cat_amnt_sum.plot(kind="bar", ax=ax[1])


# ax0 style
ax[0].set_xlabel("Categories", size=9)
ax[0].tick_params(axis="both", labelsize=8)
ax[0].set_ylabel("Count", size=9)


# ax1 style
ax[1].set_xlabel("Categories", size=9)
ax[1].tick_params(axis="both", labelsize=8)
ax[1].set_ylabel("Amount($)", size=9)
ax[1].ticklabel_format(style="plain", axis="y")

# general plot styles
plt.tight_layout(rect=[0.06, 0.05, 0.95, 0.95])
plt.suptitle("Category Barplot", size=10)

export_fig("category_freq_amnt_sum.png")

# Testing for assosciativity between categories and amount

kruskal = pg.kruskal(data=target_df, dv=target_cols[0], between=target_cols[1])

kruskal_post = sp.posthoc_dunn(
    target_df, val_col=target_cols[0], group_col=target_cols[1])
