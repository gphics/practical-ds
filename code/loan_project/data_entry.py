#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 19:29:24 2026

@author: xenon

@description: This file serves as the entry point of the project where the raw file is loaded

"""
import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent

file_path = base_dir / ".."/".." / "data"/ "loan_data.csv"

file_path = file_path.resolve()


df = pd.read_csv(file_path)
# print(base_dir)
