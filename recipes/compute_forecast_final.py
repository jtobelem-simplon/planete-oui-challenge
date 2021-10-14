# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
forecast_prepared = dataiku.Dataset("forecast_prepared")
forecast_prepared_df = forecast_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

forecast_final_df = forecast_prepared_df.pivot_table(values='status', index='timestamp', columns='station', aggfunc='first').reset_index()


# Write recipe outputs
forecast_final = dataiku.Dataset("final_automl")
forecast_final.write_with_schema(forecast_final_df)
