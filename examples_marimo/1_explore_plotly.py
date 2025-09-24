import marimo

__generated_with = "0.13.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import numpy as np
    return pl, px


@app.cell
def _(pl, px):
    iris = pl.from_pandas(px.data.iris()) 
    tips = pl.from_pandas(px.data.tips())
    gapminder = pl.from_pandas(px.data.gapminder())
    gm_oceania = gapminder.filter(pl.col("continent") == 'Oceania')
    gm_2007 = gapminder.filter(pl.col("year") == 2007)
    return gapminder, gm_2007, gm_oceania, iris, tips


@app.cell
def _(iris, px):
    px.scatter(iris, x="sepal_width", y="sepal_length")
    return


@app.cell
def _(gm_oceania, px):
    px.line(gm_oceania, x='year', y='lifeExp', color='country', markers=True)
    return


@app.cell
def _(gm_2007, px):
    px.treemap(gm_2007,
        path=[px.Constant('world'), 'continent', 'country'],
        values='pop',
        color='lifeExp', hover_data=['iso_alpha'])

    return


@app.cell
def _(px, tips):
    px.box(tips, x="time", y="total_bill", points="all")
    return


@app.cell
def _(gapminder, px):
    px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
