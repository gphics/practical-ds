#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 18:35:13 2026

@author: xenon
"""


def main_func(df, sample_frac=0.5):
    sample_df = df.sample(frac=sample_frac, replace=True)

    return sample_df
