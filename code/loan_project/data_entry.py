#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 19:29:24 2026

@author: xenon

@description: This file serves as the entry point of the project where the raw file is loaded

"""
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent

file_path = base_dir / ".."/".." / "data" / "loan_data.csv"

file_path = file_path.resolve()

df = pd.read_csv(file_path)
# print(base_dir)


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
