import marimo

__generated_with = "0.13.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl
    import numpy as np
    import plotly.express as px
    import lets_plot
    import importlib

    # Get the __all__ list from lets_plot
    all_symbols = lets_plot.__all__

    # Import each symbol into the current namespace
    for symbol in all_symbols:
        globals()[symbol] = getattr(lets_plot, symbol)
    return np, pl, px


@app.cell
def _(np, pl):
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
    return


@app.cell
def _(pl, px):
    # Data from Plotly
    iris = pl.from_pandas(px.data.iris()) 
    tips = pl.from_pandas(px.data.tips())
    gapminder = pl.from_pandas(px.data.gapminder())
    gm_oceania = gapminder.filter(pl.col("continent") == 'Oceania')
    gm_2007 = gapminder.filter(pl.col("year") == 2007)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Now lets try to create plots with plotly data in lets-plot code.""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Lets try to plot the lets plot data in plotly""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
