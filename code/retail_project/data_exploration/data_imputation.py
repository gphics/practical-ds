#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 11:42:32 2026

@author: xenon

@description: This folder is for cleaning the data

"""
import sys
from pathlib import Path
from data_entry import df as raw_df

parent_dir = Path(__file__).resolve().parent.parent
print(parent_dir)
sys.path.append(str(parent_dir))

df = raw_df.copy()


# Handling cancelled transactions

# creating a new column to determine cancellation status
df["is_cancelled"] = (df["Quantity"] < 0).astype(int)


# Removing transactions without description
df = df.dropna(subset=["Description"])


# Handling rows without customer id

# creating a new column to represent guest status
df["is_guest"] = df["Customer ID"].isnull().astype(int)

# filling the missing customer id with arbitary value
arbitary_value = 00000
df["Customer ID"] = df["Customer ID"].fillna(arbitary_value)


# spreading the date columns into single columns
target = df["InvoiceDate"]

# year of transaction
df["year"] = target.dt.year
# month of transaction
df["month_name"] = target.dt.month_name()
df["month"] = target.dt.month
# name of day of transaction
df["day_name"] = target.dt.day_name()
# day of week (int) of transaction
df["week_day"] = target.dt.weekday
# day of week (int) of transaction
df["hour"] = target.dt.hour


# saving cleaned data to the data dir
save_to = parent_dir / ".." / ".." / "data" / "cleaned_online_retail.csv"

df.to_csv(save_to, index=False)

# print(df.isnull().mean() * 100)
