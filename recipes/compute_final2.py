# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
ytest_joined_prepared_scored = dataiku.Dataset("ytest_joined_prepared_scored")
ytest_joined_prepared_scored_df = ytest_joined_prepared_scored.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

final2_df = ytest_joined_prepared_scored_df.pivot_table(values='prediction', index='timestamp', columns='station', aggfunc='first').reset_index()


# Write recipe outputs
final2 = dataiku.Dataset("finalxgb")
final2.write_with_schema(final2_df)
