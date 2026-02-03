#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 22:12:45 2026

@author: xenon
"""

from data_entry import import_df
import sys
from pathlib import Path
import pingouin as pg


parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

# Task:
"""
Medication Patterns: For a specific condition like "Asthma," what is the most frequently prescribed Medication, and does it impact the length of the stay?
"""

target_cols = ["Medical Condition", "Medication", "Admission Duration(INT)"]
target_df = import_df(target_cols)


medication_condition_group = target_df.groupby(target_cols[:2]).size()


med_vs_adm_duration = pg.kruskal(
    target_df, dv=target_cols[-1], between=target_cols[1])

med_vs_adm_duration
