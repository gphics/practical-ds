#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 21:32:10 2026

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

# Task
"""
1. Distance Logic: What is the average distance between a user's home (lat/long) and the merchant's location?

2. State-Level Trends: Are there specific states or cities that exhibit significantly higher average transaction values?
"""

target_cols = ["geo_offset(km)", "city", "state", "amt"]
target_df = import_df(target_cols)

# 1.
geo_offset_sum_stat = target_df[target_cols[0]].mean()


# 2.

# using transaction amount ($)
city_group = target_df.groupby(target_cols[1])[
    target_cols[-1]].sum().sort_values(ascending=False)

state_group = target_df.groupby(
    target_cols[2])[target_cols[-1]].sum().sort_values(ascending=False)


_, ax = plt.subplots(1, 2)

city_group[:5].plot(kind="bar", ax=ax[0])

state_group[:5].plot(kind="bar", ax=ax[1])

# ax0 style
ax[0].tick_params(labelsize=8, axis="both")
ax[0].set_ylabel("Amount($)", size=8)
ax[0].set_xlabel("City", size=8)

# ax style
ax[1].tick_params(labelsize=8, axis="both")
ax[1].set_ylabel("Amount($)", size=8)
ax[1].set_xlabel("State", size=8)

# general styles
plt.tight_layout(rect=(0.05, 0.05, 0.95, 0.95))
plt.suptitle("City & State Level Trends", size=10)

export_fig("city_state_transaction_amount.png")


# using frequency
city_group = target_df.groupby(
    target_cols[1]).size().sort_values(ascending=False)
state_group = target_df.groupby(
    target_cols[2]).size().sort_values(ascending=False)

# # # # plotting figs
# _, ax = plt.subplots(1, 2)

# city_group[:5].plot(kind="bar", ax=ax[0])

# state_group[:5].plot(kind="bar", ax=ax[1])

# # ax0 style
# ax[0].tick_params(labelsize=8, axis="both")
# ax[0].set_ylabel("Count", size=8)
# ax[0].set_xlabel("City", size=8)

# # ax style
# ax[1].tick_params(labelsize=8, axis="both")
# ax[1].set_ylabel("Count", size=8)
# ax[1].set_xlabel("State", size=8)

# # general styles
# plt.tight_layout(rect=(0.05, 0.05, 0.95, 0.95))
# plt.suptitle("City & State Level Trends", size=10)

# export_fig("city_state_transaction_freq.png")
