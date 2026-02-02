#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:52:45 2026

@author: xenon
"""
from data_entry import get_df_info, import_df
import sys
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from category_encoders import BinaryEncoder
from sklearn.feature_selection import mutual_info_classif
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)

df = import_df(drop=True)

#
#
# FEATURE EXTRACTION


X_train, X_test, y_train, y_test = train_test_split(
    df.drop("is_fraud", axis=1),
    df["is_fraud"], test_size=0.3)

ohe_cols = ["category", "gender"]

binary_cols = ["street", "state", "city", "job"]

ohe_encoder = OneHotEncoder(sparse_output=False, drop="first")
binary_encoder = BinaryEncoder()
transformers = [
    ("ohe", ohe_encoder, ohe_cols),
    ("binary", binary_encoder, binary_cols)
]

ct = ColumnTransformer(transformers=transformers,
                       remainder="passthrough", verbose_feature_names_out=False)

# setting output as pandas
ct.set_output(transform="pandas")


X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)


#
#
# FEATURE SELECTION
m_info = mutual_info_classif(X_train, y_train)

res = pd.DataFrame()
res["feature"] = X_train.columns.to_list()
res["score"] = m_info

# print(res.sort_values("score", ascending=False))


parent_features = [col.split("_")[0] for col in res["feature"]]

scores = res.groupby(parent_features)[
    "score"].sum().sort_values(ascending=False)


orig_selected_cols = [
    "state",
    "job",
    "city"
    "zip",
    "amt",
    "off_hour",
    "street",
    "city_pop",
    "age"
]

selected_cols = []
for colname in res["feature"]:
    for orig_col_name in orig_selected_cols:
        if orig_col_name in colname:
            selected_cols.append(colname)


# subsetting the dfs base on selected cols

X_train = X_train[selected_cols]
X_test = X_test[selected_cols]

xg_model = XGBClassifier()

xg_model.fit(X_train, y_train)

y_pred = xg_model.predict(X_test)

report = classification_report(y_test, y_pred)
print(report)
