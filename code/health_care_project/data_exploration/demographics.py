#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 16:43:47 2026

@author: xenon
"""
from data_entry import import_df, export_fig
import sys
from pathlib import Path
from scipy.stats import chi2_contingency, pointbiserialr
import pandas as pd
from scipy.stats.contingency import association
import pingouin as pg
import matplotlib.pyplot as plt
import seaborn as sns


parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)


# Task:
"""
    Demographic Profiling: Does a specific age group or gender correlate with higher rates of certain conditions (e.g., are older patients more frequently admitted for "Diabetes" or "Hypertension")?
 """

target_cols = ["Age", "Age Group", "Gender", "Medical Condition"]
target_df = import_df(target_cols)
# target_df = target_df.sample(frac=0.1)


# using age group
first_contingency_table = pd.crosstab(
    index=target_df[target_cols[1]], columns=target_df[target_cols[3]])

cell_counts = 8 * 6


# the pvalue gotten is above the significant level hence I fail to reject the null hypothesis and no further post hoc
_, chi_pvalue, _, expected_freq = chi2_contingency(first_contingency_table)


# using the age values
# target_df[target_cols[0]].plot(kind="hist")

age_condition_anova = pg.anova(
    data=target_df, dv=target_cols[0], between=target_cols[3], detailed=True)


# using gender
contingency_table = pd.crosstab(
    index=target_df[target_cols[2]], columns=target_df[target_cols[3]])

_, chi_pvalue, _, expected_freq = chi2_contingency(contingency_table)


# plotting graphs

# Age vs Medical conditions

first_contingency_table[:4].plot(kind="bar")
plt.title("Age Group vs Medical Condition 1")
plt.ylabel("Count")
export_fig("age_group_vs_med_cond1.png")

# first_contingency_table[4:].plot(kind="bar")
# plt.title("Age Group vs Medical Condition 2")
# plt.ylabel("Count")
# export_fig("age_group_vs_med_cond2.png")

# plotting ..

# contingency_table.plot(kind="bar")
# plt.title("Gender vs Medical Condition")
# plt.ylabel("Count")

# export_fig("gender_vs_med_cond.png")
