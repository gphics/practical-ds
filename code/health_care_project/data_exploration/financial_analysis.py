#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 21:18:26 2026

@author: xenon
"""

from data_entry import import_df, export_fig
import sys
from pathlib import Path
from scipy.stats import shapiro
import pingouin as pg
import matplotlib.pyplot as plt


parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

# Task:
"""
Financial Analysis: What is the distribution of Billing Amounts? Are certain Insurance Providers (e.g., Cigna vs. Medicare) associated with more expensive treatments or longer stays?

"""
target_cols = ["Billing Amount",
               "Insurance Provider", "Admission Duration(INT)"]
target_df = import_df(target_cols)


# Dist of billing amount
# _, ax = plt.subplots(1, 2, figsize=(13,9))
# target_df[target_cols[0]].plot(kind="hist", ax=ax[0])
# target_df[target_cols[0]].plot(kind="kde", ax=ax[1])
# plt.tight_layout(rect=[0,0.95,0,0.95])

# plt.suptitle("Billing Amount Distribution")
# export_fig("billing_amnt_dist.png")

# testing for normal distribution
# normalcy_test = shapiro(target_df[target_cols[0]])

# calculating the summary statistics
sum_stat = target_df[target_cols[0]].describe()

# Assosciation between insurance providers and billing amnt or admission duration

insurance_billing_test = pg.kruskal(
    data=target_df, dv=target_cols[0], between=target_cols[1])


insurance_adm_duration_test = pg.kruskal(
    data=target_df, dv=target_cols[0], between=target_cols[-1])

insurance_adm_duration_test
