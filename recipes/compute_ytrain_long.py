# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
ytrain_NpxebDC = dataiku.Dataset("ytrain_NpxebDC")
ytrain_NpxebDC_df = ytrain_NpxebDC.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

ytrain_long_df = ytrain_NpxebDC_df # For this sample code, simply copy input to output

pd.melt(ytrain_NpxebDC_df, id_vars=['timestamp'], var_name='station', value_name='status')


# Write recipe outputs
ytrain_long = dataiku.Dataset("ytrain_long")
ytrain_long.write_with_schema(ytrain_long_df)
