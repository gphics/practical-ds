#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 18:32:23 2026

@author: xenon
"""
import seaborn as sns
import pandas as pd
import numpy as np
from boostrap import main_func as bootstrap

file_path = "../data/loan_data.csv"


df = pd.read_csv(file_path)

target = df["person_income"]

target.plot(kind="hist", bins=30)

# target_median = target.median()
# print(target_median)

# res = []

# for _ in range(1000):
#     sample = bootstrap(target)
#     res.append(sample.median())

# print(np.median(res))
