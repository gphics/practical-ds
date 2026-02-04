#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:28:45 2026

@author: xenon


"""
from data_entry import import_df, get_df_info, export_fig
import sys
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pointbiserialr
import pandas as pd

parent_dir = str(Path(__file__).resolve().parent.parent)

sys.path.append(parent_dir)


# Task
"""
Environmental Impact Studies: Examine the link between a country's agricultural land percentage, forested area, and its CO2 emissions to understand environmental footprints.

"""

target_cols = [
    "Country", "Agricultural Land( %)", "Forested Area (%)", "Co2-Emissions", "Urban_population"]
target_df = import_df(target_cols)

sns.heatmap(target_df[target_cols[1:]].corr(), annot=True)
plt.title("Environmental Impacts")
export_fig("environmental_impacts_heatmap.png")

# subsetting df and getting the top 10
urban_sorted_top_10 = target_df.sort_values(
    by=target_cols[-1], ascending=False)[["Urban_population", "Country"]].head(10)

co2_sorted_top_10 = target_df.sort_values(
    by=target_cols[-2], ascending=False)[["Co2-Emissions", "Country"]].head(10)

# print(co2_sorted_top_10) Tuvalu
# print(urban_sorted_top_10) Liechtenstein

# Plotting the graphs
# _, ax = plt.subplots(1, 2)

# # Actual graph plotting
# sns.barplot(co2_sorted_top_10, x = target_cols[0], y = target_cols[-2], ax=ax[0])

# sns.barplot(urban_sorted_top_10, x = target_cols[0], y = target_cols[-1], ax=ax[1])

# # styling ax 0
# ax[0].tick_params(rotation=90, axis="x", labelsize=7)
# ax[0].tick_params(axis="y", labelsize=7)
# ax[0].ticklabel_format(axis="y", style="plain")
# ax[0].set_xlabel("Country", size=8)
# ax[0].set_ylabel("CO2 Emission", size=8)


# # styling ax 1
# ax[1].tick_params(rotation=90, axis="x", labelsize=7)
# ax[1].tick_params(axis="y", labelsize=7)
# ax[1].ticklabel_format(axis="y", style="plain")
# ax[1].set_xlabel("Country", size=8)
# ax[1].set_ylabel("Urban Population", size=8)

# # general styles
# plt.tight_layout(rect=(0.05,0.05, 0.95,0.95))
# plt.suptitle("CO2 Emission & Urban Population By Country (Top 10)", size=10)

# export_fig("co2_emission_&_urban_pop_barplot.png")


# Task 2
"""

Impact of urban population on life expectancy

"""
target_cols = ["Country", "Urban_population",
               "Co2-Emissions", "Life expectancy"]

target_df = import_df(target_cols)
cond = target_df.loc[target_df["Country"] == "China"]

corr_df = target_df[target_cols[1:]].corr()

# sns.heatmap(corr_df, annot=True)

# plt.title("Environmental Impacts 2")
# export_fig("environmental_impacts_heatmap_2.png")

subset_df = target_df[["Country", "Life expectancy"]]

# countries with the lowest life expectancy
smallest = subset_df.nsmallest(
    10, "Life expectancy").sort_values("Life expectancy", ascending=False)

# countries with the highest life expectancy
highest = subset_df.nlargest(10, "Life expectancy").sort_values(
    "Life expectancy", ascending=False)

# Plotting the graphs
# _, ax = plt.subplots(1, 2)

# # Actual graph plotting
# sns.barplot(highest, x=target_cols[0], y=target_cols[-1], ax=ax[0])

# sns.barplot(smallest, x=target_cols[0], y=target_cols[-1], ax=ax[1])

# # styling ax 0
# ax[0].tick_params(rotation=90, axis="x", labelsize=7)
# ax[0].tick_params(axis="y", labelsize=7)
# ax[0].ticklabel_format(axis="y", style="plain")
# ax[0].set_xlabel("Country (Top) ", size=8)
# ax[0].set_ylabel("Life Expectancy", size=8)


# # styling ax 1
# ax[1].tick_params(rotation=90, axis="x", labelsize=7)
# ax[1].tick_params(axis="y", labelsize=7)
# ax[1].ticklabel_format(axis="y", style="plain")
# ax[1].set_xlabel("Country (Bottom)", size=8)
# ax[1].set_ylabel("Life Expectancy", size=8)

# # general styles
# plt.tight_layout(rect=(0.05, 0.05, 0.95, 0.95))
# plt.suptitle("Life Expectancy By Country (Top & Bottom 10)", size=10)

# export_fig("top_&_bottom_life_expectancy_by_country.png")


# Task

"""
Further investigate the top and bottom predictors for life expectancy
"""

target_df = import_df()


# selecting numerical features
target_df = target_df.select_dtypes(exclude="O")

# the target feature
target_col = "Life expectancy"

# getting the predictor cols
predictor_cols = target_df.columns.to_list()

# # removing the target col from the predictor cols
predictor_cols.remove(target_col)

# initialising storage list
corr_coef = []

# performing a loop over predictor cols
for col in predictor_cols:
    coef, _ = pointbiserialr(target_df[col], target_df[target_col])
    corr_coef.append(coef)

# creating a df to store the result of the ops
corr_df = pd.DataFrame()
corr_df["predictor"] = predictor_cols
corr_df["coef"] = corr_coef

# subsetting df
top_10_predictors = corr_df.nlargest(
    10, "coef").sort_values("coef", ascending=False)

bottom_10_predictors = corr_df.nsmallest(
    10, "coef").sort_values("coef", ascending=False)


# Plotting the graphs
# _, ax = plt.subplots(1, 2)

# # Actual graph plotting
# sns.barplot(top_10_predictors, x="predictor", y="coef", ax=ax[0])

# sns.barplot(bottom_10_predictors,  x="predictor", y="coef", ax=ax[1])

# # styling ax 0
# ax[0].tick_params(rotation=90, axis="x", labelsize=7)
# ax[0].tick_params(axis="y", labelsize=7)
# ax[0].ticklabel_format(axis="y", style="plain")
# ax[0].set_xlabel("Predictor(Top)", size=8)
# ax[0].set_ylabel("Correlation Coeficient", size=8)


# # styling ax 1
# ax[1].tick_params(rotation=90, axis="x", labelsize=7)
# ax[1].tick_params(axis="y", labelsize=7)
# ax[1].ticklabel_format(axis="y", style="plain")
# ax[1].set_xlabel("Predictor(Bottom)", size=8)
# ax[1].set_ylabel("Correlation Coeficient", size=8)
# # general styles
# plt.tight_layout(rect=(0.05, 0.05, 0.95, 0.95))
# plt.suptitle("Life Expectancy By Country (Top & Bottom 10)", size=10)

# export_fig("top_&_bottom_predictors_for_life_expectancy.png")
