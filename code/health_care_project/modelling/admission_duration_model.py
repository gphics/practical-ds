#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 22:30:36 2026

@author: xenon
"""

import sys
from pathlib import Path
from sklearn.feature_selection import mutual_info_regression

base_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(base_dir)


cols_to_drop = ["Name", "Age Group", "Admission Duration", "Room Number"]
