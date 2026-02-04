#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:06:12 2026

@author: xenon
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


base_dir = Path(__file__).resolve().parent

data_file_path = base_dir / ".." / ".." / "data/credit_card_transactions.csv"


df = pd.read_csv(data_file_path, parse_dates=[
                 "trans_date_trans_time", "dob"])

# df = pd.read_csv(data_file_path, parse_dates=[
#                  # "trans_date_trans_time", "dob"])


# Feature engineering for transaction date
df["year"] = df["trans_date_trans_time"].dt.year
df["month"] = df["trans_date_trans_time"].dt.month
df["hour"] = df["trans_date_trans_time"].dt.hour

# weeks
df["day_name"] = df["trans_date_trans_time"].dt.day_name()
df["week_day"] = df["trans_date_trans_time"].dt.weekday

# months
df["month_day"] = df["trans_date_trans_time"].dt.day


# determing off-hour
# standard hour < 7 or hour >= 22
off_hour_condition = (df["hour"] < 7) | (df["hour"] >= 22)
df["off_hour"] = off_hour_condition

# calculating weekend
df["is_weekend"] = df["week_day"].isin([5, 6])


# calculating customer age
df["age"] = df["year"] - df["dob"].dt.year


# determining the distance between the merchant and the customer
# saving it as geo_offset

def haversine_vectorized(cust_lat, cust_long, merch_lat, merch_long):
    """
    This function is for calculating the distance between customer and merchant from their lat and long
    """
    R = 6371  # Earth radius in km
    phi1, phi2 = np.radians(cust_lat), np.radians(merch_lat)
    dphi = np.radians(merch_lat - cust_lat)
    dlambda = np.radians(merch_long - cust_long)

    a = np.sin(dphi/2.0)**2 + np.cos(phi1) * \
        np.cos(phi2) * np.sin(dlambda/2.0)**2
    return 2 * R * np.arcsin(np.sqrt(a))


target_cols = ["lat", "long", "merch_lat", "merch_long"]
target_df = df[target_cols]
df["geo_offset(km)"] = haversine_vectorized(
    target_df[target_cols[0]],
    target_df[target_cols[1]],
    target_df[target_cols[2]],
    target_df[target_cols[3]]
)

# classifying transaction base on the amount spent
bins = [1, 9.65, 40.75, 83.75, np.inf]
labels = ["bronze", "silver", "gold", "plantinum"]
df["spending_class"] = pd.cut(df["amt"], bins=bins, labels=labels)


def import_df(cols=[], drop=False):
    """
    @description: This function is responsible for copying and importing the dataset.
    @params: 
        cols: An optional parameter containing list of columns to import
        drop: bool, default is False. It signifies to drop some columns which is irrelevant for model building.
    @returns: DF
    """
    irrelevant_cols = ["cc_num", "first", "last",  "dob", "unix_time", "day_name", "week_day",
                       "lat", "long", "merch_lat", "merch_long", "merch_zipcode", "trans_date_trans_time", "Unnamed: 0", "merchant", "trans_num", "spending_class"]
    new_df = None
    if len(cols):
        new_df = df[cols].copy()
    else:
        new_df = df.copy()

    # if the imported df is for modelling
    if not len(cols) and drop:
        new_df = new_df.drop(irrelevant_cols, axis=1)
    return new_df


def get_df_info():
    """
    This function is for printing the information about the entire dataset
    """
    print(df.info())


# setting plot styles
sns.set_theme(style="ticks", palette="viridis")


def export_fig(fig_name: str) -> None:
    """
    @params: 
        fig_name: Name to save the figure with

    @description:
        This function is responsible for saving plot figures to the visuals directories

    @returns:
        None
    """

    save_to_path = str(base_dir) + "/visuals/{}".format(fig_name)
    plt.savefig(save_to_path, dpi=350, bbox_inches="tight")
