#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:21:16 2026

@author: xenon
"""

import sys
from pathlib import Path
from main_entry import export_df, export_fig
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

df = export_df()

# removing rows with cancelled transactions
removal_condition = df["is_cancelled"] == True
df = df[~removal_condition]

# Task 1
"""
Top & Bottom Performers: Which products are the best-sellers by quantity (frequency of occurence) ?
"""

target_cols = ["Description", "Quantity"]
target_df = df[target_cols]


product_performance_by_freq = target_df[target_cols[0]
                                        ].value_counts()
product_performance_by_quantity = target_df.groupby(target_cols[0])[
    target_cols[1]].sum()
# print(product_performance_by_quantity)


def get_rank(df, size="large"):
    if size == "large":
        return df.nlargest(10)
    else:
        return df.nsmallest(10)


# Ranking base on frequency
freq_top_performance = get_rank(product_performance_by_freq)
freq_bottom_performance = get_rank(product_performance_by_freq, "small")

# Quantity Ranking
quantity_top_performance = get_rank(product_performance_by_quantity)
quantity_bottom_performance = get_rank(
    product_performance_by_quantity, "small")

# quantity_top_performance.plot(kind="bar")
# plt.xticks(size=7)
# plt.xlabel("Products")
# plt.title("Top Product Performance by Quantity")
# export_fig("top_product_performance_by_quantity.png")

# print(freq_top_performance.head(1))
# print(freq_bottom_performance.head(1))
# print(quantity_top_performance.head(1))
# print(quantity_bottom_performance.head(1))
