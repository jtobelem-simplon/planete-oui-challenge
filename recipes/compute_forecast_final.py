# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
forecast_by_station = dataiku.Dataset("forecast_by_station")
forecast_by_station_df = forecast_by_station.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

forecast_final_df = forecast_by_station_df.rename(lambda x : x.split('_')[0], axis='columns')


# Write recipe outputs
forecast_final = dataiku.Dataset("forecast_final")
forecast_final.write_with_schema(forecast_final_df)
