#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:22:07 2026

@author: xenon
"""
import sys
from pathlib import Path
from main_entry import export_df, export_fig
import matplotlib.pyplot as plt
import seaborn as sns

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

df = export_df()


# Task 1:
"""
Monthly Trends: Which months see the highest transaction volume?

"""

target_cols = ["month_name", "year", "InvoiceDate"]
target_df = df[target_cols]

monthly_transaction_volume = target_df["month_name"].value_counts()


# plotting the bar-graph of monthly_transaction_volume
# monthly_transaction_volume.plot(kind="bar")
# plt.title("Monthly Transaction Volume")
# export_fig("monthly_transaction_volume.png")


# Task 2:
"""
Peak Activity Times: What are the busiest days of the week and hours of the day for sales?
"""
target_cols = ["day_name", "hour"]
target_df = df[target_cols]

# calculating the busiest hours in each day
busiest = target_df.groupby(target_cols).size()
# subseting the top 10
top_10 = busiest.nlargest(10)

# plotting the bar plot of the top 10 busiest hours
# top_10.plot(kind="bar")
# plt.title("top 10 busiest hours with days".title())
# export_fig("busiest_hours.png")


# Task 3:
"""

"""
