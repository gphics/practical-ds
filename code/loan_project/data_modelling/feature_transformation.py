#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 15:18:33 2026

@author: xenon
"""
from data_entry import df as raw_df
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt

base_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(base_dir)

df = raw_df.copy()

X_train, X_test, y_train, y_test = train_test_split(
    df.drop("loan_status", axis=1), df["loan_status"], test_size=0.3)

# selecting 'object' cols for encoding
ordinal_cols = ["person_education"]
education_order = ['High School', 'Associate',
                   'Bachelor', 'Master', 'Doctorate']
ohe_cols = ["person_gender",
            "previous_loan_defaults_on_file", "person_home_ownership", "loan_intent"]

# selecting 'number' cols for transformation
num_cols = X_train.select_dtypes(exclude="O").columns.to_list()


def create_pairplot(df, trans="before"):
    """
    This function is for creating pairplot and saving it.
    """
    df[num_cols].hist(figsize=(12, 10))
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.suptitle(
        "Pairplot showing the data distributions of all continous variables".title())
    plt.savefig(f"{base_dir}/visuals/pairplot_{trans}_trans.png")

# create_pairplot(X_train)


# creating encoders
ohe_encoder = OneHotEncoder(sparse_output=False, drop="first")
ord_encoder = OrdinalEncoder(categories=[education_order])
num_transformer = PowerTransformer()


# setting the transformers
transformers = [
    ("ohe", ohe_encoder, ohe_cols),
    ("ord", ord_encoder, ordinal_cols),
    ("num", num_transformer, num_cols)

]

ct = ColumnTransformer(
    transformers=transformers, remainder="passthrough", verbose_feature_names_out=False
)
ct.set_output(transform="pandas")

# encoding features
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# create_pairplot(X_train, "after")

# X_train.info()
