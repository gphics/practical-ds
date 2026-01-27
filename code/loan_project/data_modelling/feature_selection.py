#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 16:20:54 2026

@author: xenon
"""
import sys
from pathlib import Path
import pandas as pd
from feature_transformation import X_train,  y_train
from sklearn.feature_selection import mutual_info_classif, SelectKBest
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(49)


base_dir = str(Path(__file__).resolve().parent.parent)
# sys.path.append(base_dir)
mi_classif = mutual_info_classif(X_train, y_train)
kbest = SelectKBest(score_func=mutual_info_classif, k=7)

kbest.fit(X_train, y_train)

kbest_scores = kbest.scores_

score_df = pd.DataFrame()
score_df["feature"] = X_train.columns.to_list()
score_df["mi"] = mi_classif
score_df["kbest"] = kbest_scores


# plotting graph
# sns.barplot(score_df.sort_values(by="kbest", ascending=False), x="feature", y="kbest")
# plt.title("Feature selection using Select KBest".title())
# plt.xticks(rotation=90, size=9)
# plt.savefig(f"{base_dir}/visuals/feature_selection_kbest.png")


def final_selection(by="mi"):
    subset_df = score_df.nlargest(n=6, columns=by)
    selected_cols = subset_df["feature"].to_list()
    return selected_cols


# The two feature selection method selected the same data
kbest_selected = final_selection("kbest")
mi_selected = final_selection()

# since one of the home ownership values was selected, the rest are also added.
home_ownership = ["person_home_ownership_OTHER", "person_home_ownership_OWN"]


features_selected = mi_selected + home_ownership
print(features_selected)
