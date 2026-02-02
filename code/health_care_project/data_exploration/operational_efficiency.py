#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 20:44:00 2026

@author: xenon
"""

import sys
from pathlib import Path
from data_entry import import_df
import pingouin as pg


parent_dir = Path(__file__).resolve().parent.parent

sys.path.append(str(parent_dir))

# Task:
"""
Operational Efficiency: How many Hospitals or Doctors have the longest average admission durations, and is there a correlation with the Medical Condition being treated?
"""

target_cols = ["Hospital", "Doctor",
               "Medical Condition", "Admission Duration(INT)"]

target_df = import_df(target_cols)

# Average admission duration

# Using hospitals
hospital_group = target_df.groupby(target_cols[0])[target_cols[-1]].mean()

# Using Doctor

doctor_group = target_df.groupby(target_cols[1])[target_cols[-1]].mean()


# Correlation between Admission duration and Medical condition

# Type casting the admission duration from time-delta to int

target_df[target_cols[-1]].plot(kind="hist")

# Non-parametric test to check for relationship between admission duration and medical condition
kruskal_test = pg.kruskal(
    data=target_df, dv=target_cols[-1], between=target_cols[-2])
kruskal_test
