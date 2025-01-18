# %%
import polars as pl
import numpy as np
from lets_plot import *
LetsPlot.setup_html()

# %%
# Data
np.random.seed(12)
data_a200 = pl.DataFrame({"rating": np.random.normal(0, 1, 200)}).with_columns(cond = pl.lit("A"))
data_b200 = pl.DataFrame({"rating": np.random.normal(1, 1.5, 200)}).with_columns(cond = pl.lit("B"))
data_ab200 = pl.concat([data_a200, data_b200])

# https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/cookbook/histogram.ipynb
np.random.seed(42)
data_a100 = pl.DataFrame({"x": np.random.normal(-0.5, 1, 100), "y":np.random.normal(0, 1, 100)}).with_columns(cat = pl.lit("A"))
data_b100 = pl.DataFrame({"x": np.random.normal(0.5, 1, 100), "y":np.random.normal(0, 1, 100)}).with_columns(cat = pl.lit("B"))

data_ab100 = pl.concat([data_a100, data_b100])

# %%
ggplot(data_ab200, aes(x='rating', fill='cond')) + \
  ggsize(700, 300) + \
  geom_density(color='dark_green', alpha=.7) + \
  scale_fill_brewer(type='seq') + \
  theme(panel_grid_major_x='blank')

# %%
p = ggplot(data_ab100, aes('x', fill='cat'))
p + geom_point(aes(y='y', color='cat'), size=3, alpha=0.8) + \
    ggtitle('Scatter plot')

# %%
p + geom_histogram() + ggtitle('Default histogram')

# %%
p + geom_histogram(alpha=0.5, position='identity') + \
    ggtitle('Overlaid semi transparent histogram')

