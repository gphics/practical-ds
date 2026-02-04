#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 19:55:19 2026

@author: xenon
"""
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


base_dir = Path(__file__).resolve().parent

file_path = base_dir / ".." / ".." / "data/world-data-2023.csv"

df = pd.read_csv(file_path)

irrelevant_cols = ["Abbreviation", "Calling Code",
                   "Capital/Major City", "Capital/Major City", "Currency-Code"]


# dropping useless cols
df = df.drop(irrelevant_cols, axis=1)


# Removing unnecessary symbols and transforming certain cols to float dtype

# selecting object cols
cols_with_symbols = df.select_dtypes(include="O").columns.to_list()

# Removing cols that are truly object
cols_with_symbols.remove("Country")
cols_with_symbols.remove("Largest city")
cols_with_symbols.remove("Official language")


def remove_symbols(x):
    """
    This function receives a column, removes the % sign in it and transform it from object to float
    """
    res = x.str.replace(r'[^0-9.]', '', regex=True)
    return res.astype(float)


# transforming cols
df[cols_with_symbols] = df[cols_with_symbols].apply(remove_symbols)


# # Handling missing data
percentage_null = df.isnull().mean() * 100

# getting the overall missing cols
null_cols = percentage_null[percentage_null > 0.0].index
missing_df = df[null_cols]

# # subsetting missing cols base on dtype
num_null_cols = missing_df.select_dtypes(exclude="O").columns.to_list()

str_null_cols = missing_df.select_dtypes(include="O").columns.to_list()

# # splitting data
X_train, X_test = train_test_split(df, test_size=0.3)

# IMPUTATION
transformers = [
    ("num", SimpleImputer(), num_null_cols),
    ("cat", SimpleImputer(strategy="most_frequent"), str_null_cols)
]

# initialising pipeline
ct = ColumnTransformer(transformers, remainder="passthrough",
                       verbose_feature_names_out=False)

ct.set_output(transform="pandas")

# fitting and transform data
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# creating a cleaned data
cleaned_df = pd.concat([X_train, X_test], ignore_index=True)

# print(cleaned_df["Co2-Emissions"].unique())

# creating a function to export a copy of the cleaned data


def import_df(cols=[]):
    final_df = None
    if len(cols):
        final_df = cleaned_df[cols].copy()
    else:
        final_df = cleaned_df.copy()
    return final_df


def get_df_info():
    return cleaned_df.info()


sns.set_palette("magma")


def export_fig(figname):
    file_path = str(base_dir) + "/visuals/{}".format(figname)

    plt.savefig(file_path, dpi=350, bbox_inches="tight")
