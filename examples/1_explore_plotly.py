# %%
!pip3 install plotly --upgrade

# %%
import polars as pl
import plotly.express as px
import numpy as np

iris = pl.from_pandas(px.data.iris()) 
tips = pl.from_pandas(px.data.tips())
gapminder = pl.from_pandas(px.data.gapminder())
gm_oceania = gapminder.filter(pl.col("continent") == 'Oceania')
gm_2007 = gapminder.filter(pl.col("year") == 2007)

# %%
px.scatter(iris, x="sepal_width", y="sepal_length")

# %%
px.line(gm_oceania, x='year', y='lifeExp', color='country', markers=True)


# %%
px.treemap(gm_2007, path=[px.Constant('world'), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'])

# %%
px.box(tips, x="time", y="total_bill", points="all")

# %%
px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
# %%
