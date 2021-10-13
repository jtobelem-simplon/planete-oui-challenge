# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
yrandom = dataiku.Dataset("yrandom")
yrandom_df = yrandom.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

yrandom_long_df = yrandom_df.melt(id_vars=['timestamp'], var_name='station', value_name='status')


# Write recipe outputs
yrandom_long = dataiku.Dataset("yrandom_long")
yrandom_long.write_with_schema(yrandom_long_df)
