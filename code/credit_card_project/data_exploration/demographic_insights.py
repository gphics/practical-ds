#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 08:51:29 2026

@author: xenon
"""

from data_entry import import_df, export_fig, get_df_info
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import seaborn as sns
import numpy as np
import pingouin as pg
import scikit_posthocs as sp


parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

# Task:
"""
Demographic Insights
1. Age vs. Spending: Is there a correlation between the cardholder’s age (derived from dob) and their preferred spending categories?

2. Gender Bias: Do spending patterns in categories like travel or food_dining differ significantly between genders?
"""

target_cols = ["gender", "year", "category", "amt", "age"]

target_df = import_df(target_cols)

# target_df = target_df.sample(frac=0.3)

# 1.
age_cat_anova = pg.anova(target_df, dv=target_cols[-1], between=target_cols[2])

print(age_cat_anova)
post_hoc = pg.pairwise_tukey(
    target_df, dv=target_cols[-1], between=target_cols[2])

# 2.
gender_cat_amt_anova = pg.anova(
    target_df, dv=target_cols[-2], between=[target_cols[0], target_cols[2]])
gender_cat_amt_anova
