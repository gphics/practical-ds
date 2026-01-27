#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 19:48:24 2026

@author: xenon
"""


from data_entry import df
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
from scipy.stats import spearmanr, mannwhitneyu, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from scipy.stats.contingency import association

parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

target_cols = ["person_income", "loan_status"]

# Task 1 :
"""
Income Distribution: What is the average and median income of loan applicants, and how does it differ between those who repay and those who default?
"""

target_df = df[target_cols]

# condition for choosing applicants that repay loan
repay_condition = target_df[target_cols[1]] == 1

# subsetting the target_df base on their loan status
non_defaulters = target_df[repay_condition]
defaulters = target_df[~repay_condition]

# helper function


def get_summary_stat(df, col):
    """
    @description: This function calculate the summary statistics of a dataframe column

    @params:
            df --> pandas series or dataframe
            col ---> column name (string)

    @returns: pandas series containing the summary statistics
    """
    summary_stat = df[col].agg(["mean", "median"])
    return summary_stat

# getting summary statistics


# summary statistics for all
summary_stat = get_summary_stat(target_df, target_cols[0])

# summary statistics for subsets
non_defaulters_stat = get_summary_stat(non_defaulters, target_cols[0])
defaulters_stat = get_summary_stat(defaulters, target_cols[0])

# print(summary_stat)
# print(non_defaulters_stat)
# print(defaulters_stat)


# plotting the histogram of person_income data

# target_df[target_cols[0]].plot(kind="hist")
# plt.title("Person Income Distribution")

# saving the plot figure
# plt.savefig(f"{parent_dir}/visuals/person_income_dist.png")


# Task 2:
"""
Employment Stability: Does the length of employment or "Years at Current Job" correlate with a lower likelihood of default?

"""

target_cols = ["person_emp_exp", "loan_status"]
target_df = df[target_cols]

# plotting the histogram of  person_emp_exp

# From the histplot, it appears that the person employment experienc is right skewed i.e most people in this data have a low years of experience

# target_df[target_cols[0]].plot(kind="hist")
# plt.title("Employment Experience Histogram")
# plt.savefig(f"{parent_dir}/visuals/employment_exp_hist.png")


# using the repay condition created earlier since it only recognize loan status to subset the current target_df

defaulters = target_df[repay_condition][target_cols[0]]
non_defaulters = target_df[~repay_condition][target_cols[0]]

# calculating the correlation coeficient and significance
spearmans_stat = spearmanr(
    target_df[target_cols[0]], target_df[target_cols[0]])

# using mannwhitneyu test to test for significance
mann_significance = mannwhitneyu(defaulters, non_defaulters)


# Task 3:
"""
Education & Professional Level: How do loan default/repay rates vary across different education levels (e.g., Graduate vs. Non-Graduate)?
"""
# df.info()

# creating the subset df
target_cols = ["person_education", "loan_status"]
target_df = df[target_cols]

# creating a contingency table
contingency_table = pd.crosstab(
    target_df[target_cols[0]], target_df[target_cols[1]])

# performing chi-square test
chi_res = chi2_contingency(contingency_table)

# performing cochran armitage trend test
table = sm.stats.Table(contingency_table)

cochran_test = table.test_ordinal_association()
cochran_res = cochran_test.pvalue

# print(cochran_res)
# print(chi_res)

# Task 4:
"""
Financial Ratios: What is the average Debt-to-Income (DTI) ratio of borrowers, and at what threshold does the risk of default significantly increase?
"""
# df.info()

# loan_percent_income === DTI
target_cols = ["loan_percent_income", "loan_status"]
target_df = df[target_cols]

# getting summary stat
dti_summary_stat = target_df[target_cols[0]].agg(["mean", "median"])

# print(dti_summary_stat)
# getting threshold

# using tree model
tree_model = DecisionTreeClassifier(max_depth=1)
tree_model.fit(target_df[[target_cols[0]]], target_df[target_cols[1]])

raw_tree_threshold = export_text(tree_model, feature_names=[target_cols[0]])
tree_threshold = 0.24

# using logistic regression

trans_dti = target_df[[target_cols[0]]] * 100
log_reg = LogisticRegression()
log_reg.fit(trans_dti, target_df[target_cols[1]])

dti_range = np.linspace(0, 100, 100).reshape(-1, 1)

proba = log_reg.predict_proba(dti_range)[:, 1]

# sns.lineplot(proba)
# plt.xlabel("DTI")
# plt.ylabel("Probability")
# plt.title("Sigmoid curve for determining DTI threshold (0.24)")
# plt.savefig(f"{parent_dir}/visuals/dti_sigmoid_curve_threshold.png")


# Task 5:
"""
Regional Insights: Which home ownership shows the highest concentration of loan applications or default rates?
"""

target_cols = ["person_home_ownership", "loan_status"]
target_df = df[target_cols]

grouped_subset = target_df.groupby(
    target_cols).size().sort_values(ascending=False)

contingency_table = pd.crosstab(
    target_df[target_cols[0]], target_df[target_cols[1]])

# performing chi test
chi_test = chi2_contingency(contingency_table)

# checking the strength of associativity
strength = association(contingency_table)
# print(chi_test)
# print(strength)

# plotting the count plot of home ownership distribution
# sns.countplot(target_df, x = target_cols[0], hue=target_cols[1])
# plt.title("Count Plot Of Home Ownership")

# plt.savefig(f"{parent_dir}/visuals/home_ownership_count_plot.png")

# TASK 6:
"""
Gender influence: what is the relationship between age and whether loan applicant would repay or default ?
"""
target_cols = ["person_age", "loan_status"]
target_df = df[target_cols]

spearmans_stat = spearmanr(
    target_df[target_cols[0]], target_df[target_cols[1]])
