#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 11:38:34 2026

@author: xenon

@description: This file is for the analysis of the loan data

"""

from data_entry import df
from pathlib import Path
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, pointbiserialr
from scipy.stats.contingency import association


base_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(base_dir)
sns.set_theme(palette="husl", style="white")

# Task 1:
"""
Loan Purpose: What are the most common reasons for seeking a loan (e.g., debt consolidation, home improvement, small business), and which category has the highest risk?
"""
target_cols = ["loan_intent", "loan_status"]
target_df = df[target_cols]


def export_fig(img_name):
    img_path = f"{base_dir}/visuals/{img_name}"
    plt.savefig(img_path)


# getting the proportions of loans for each loan intent
loan_intent_bar = target_df[target_cols[0]].value_counts().sort_values()

# print(loan_intent_bar)
# plotting ...
# loan_intent_bar.plot(kind="bar")
# plt.title("Loan Intent Bar Plot")
# plt.xticks(size=9, rotation=65)
# export_fig("loan_intent_bar_plot.png")

# category with the highest risk
contingency_table = pd.crosstab(
    index=target_df[target_cols[0]], columns=target_df[target_cols[1]])


# sns.countplot(data = target_df, x = target_cols[0], hue=target_cols[1])
# plt.xticks(rotation=75, size=9)


# performing chi-square test to check the statistical significance
_, chi_pvalue, _, expected_freq = chi2_contingency(contingency_table)

# calculating the residuals
standardized_residuals = (
    contingency_table - expected_freq)/np.sqrt(expected_freq)

# creating a clean df for loan_intent and it's risk
default_df = pd.DataFrame()
default_df["loan_intent"] = standardized_residuals.index
default_df["residuals"] = standardized_residuals.iloc[:, 1].values

# reordering the dataframe
default_df.sort_values('residuals', ascending=False, inplace=True)

# print(default_df)
# plotting the loan intent risk
# sns.barplot(default_df, x="loan_intent", y="residuals")
# plt.xticks(rotation=85, size=9)
# plt.title("Chi-square Residuals For High Risk Loan Intent")
# export_fig("loan_intent_residuals.png")

# Task 2:
"""
Interest Rates: Is there a clear relationship between higher interest rates and an increase in defaults?
"""

target_cols = ["loan_int_rate", "loan_status"]
target_df = df[target_cols]

pb_corr = pointbiserialr(target_df[target_cols[0]], target_df[target_cols[1]])
