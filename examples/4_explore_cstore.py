# %%
import polars as pl
import numpy as np
import plotly.express as px

from lets_plot import *

LetsPlot.setup_html()

# %%
# Load the data: We have data for 1 week for 1 gas station

discounts = pl.read_parquet("../cstore/cstore_discounts.parquet")
payments = pl.read_parquet("../cstore/cstore_payments.parquet")
sets = pl.read_parquet("../cstore/cstore_transaction_sets.parquet")
daily = pl.read_parquet("../cstore/cstore_transactions_daily_agg.parquet")
items = pl.read_parquet("../cstore/pdi_cstore_transection_items.parquet")
shopper = pl.read_parquet("../cstore/cstore_shopper.parquet")
gtin = pl.read_parquet("../cstore/cstore_master_ctin.parquet")


# %%
# Which shopper's spent the most money, had the most transactions, bot the most soda?

# %%
# How do days of the week compare for the ratio of candy to packaged beverage sales?

# %%
# How do the hours of 7 am to 10 am compare for weekdays and weekends?