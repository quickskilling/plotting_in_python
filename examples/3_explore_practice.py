# %%
import polars as pl
import numpy as np
import plotly.express as px

from lets_plot import *

LetsPlot.setup_html()


# %%
## Data from Lets Plot
np.random.seed(12)
data_a200 = pl.DataFrame({"rating": np.random.normal(0, 1, 200)}).with_columns(cond = pl.lit("A"))
data_b200 = pl.DataFrame({"rating": np.random.normal(1, 1.5, 200)}).with_columns(cond = pl.lit("B"))
data_ab200 = pl.concat([data_a200, data_b200])

# https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/cookbook/histogram.ipynb
np.random.seed(42)
data_a100 = pl.DataFrame({"x": np.random.normal(-0.5, 1, 100), "y":np.random.normal(0, 1, 100)}).with_columns(cat = pl.lit("A"))
data_b100 = pl.DataFrame({"x": np.random.normal(0.5, 1, 100), "y":np.random.normal(0, 1, 100)}).with_columns(cat = pl.lit("B"))

data_ab100 = pl.concat([data_a100, data_b100])

# Data from Plotly
iris = pl.from_pandas(px.data.iris()) 
tips = pl.from_pandas(px.data.tips())
gapminder = pl.from_pandas(px.data.gapminder())
gm_oceania = gapminder.filter(pl.col("continent") == 'Oceania')
gm_2007 = gapminder.filter(pl.col("year") == 2007)

# %%
# Now lets try to create plots with the plotly data in Lets plot


# %%
# Lets try to plot the lets plot data in plotly