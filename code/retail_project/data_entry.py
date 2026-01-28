#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 11:20:25 2026

@author: xenon

@description: This file is the one that read the unprocessed data from the data dir and make it available for other files for consumption.

"""


import sys
from pathlib import Path
import pandas as pd


base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

data_name = "online_retail_II.csv"
file_path = base_dir / ".." / "data" / data_name


df = pd.read_csv(file_path, parse_dates=["InvoiceDate"])
