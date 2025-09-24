import marimo

__generated_with = "0.13.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import lets_plot
    import importlib

    # Get the __all__ list from lets_plot
    all_symbols = lets_plot.__all__

    # Import each symbol into the current namespace
    for symbol in all_symbols:
        globals()[symbol] = getattr(lets_plot, symbol)
    return


@app.cell
def _():
    import numpy as np
    import polars as pl
    return np, pl


@app.cell
def _(np, pl):
    np.random.seed(12)
    data_a200 = pl.DataFrame({"rating": np.random.normal(0, 1, 200)}).with_columns(cond = pl.lit("A"))
    data_b200 = pl.DataFrame({"rating": np.random.normal(1, 1.5, 200)}).with_columns(cond = pl.lit("B"))
    data_ab200 = pl.concat([data_a200, data_b200])

    # https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/cookbook/histogram.ipynb
    np.random.seed(42)
    data_a100 = pl.DataFrame({"x": np.random.normal(-0.5, 1, 100), "y":np.random.normal(0, 1, 100)}).with_columns(cat = pl.lit("A"))
    data_b100 = pl.DataFrame({"x": np.random.normal(0.5, 1, 100), "y":np.random.normal(0, 1, 100)}).with_columns(cat = pl.lit("B"))

    data_ab100 = pl.concat([data_a100, data_b100])
    return data_ab100, data_ab200


@app.cell
def _(aes, data_ab200, geom_density, ggplot, ggsize, scale_fill_brewer, theme):
    ggplot(data_ab200, aes(x='rating', fill='cond')) + \
      ggsize(700, 300) + \
      geom_density(color='dark_green', alpha=.7) + \
      scale_fill_brewer(type='seq') + \
      theme(panel_grid_major_x='blank')
    return


@app.cell
def _(aes, data_ab100, geom_point, ggplot, ggtitle):
    p = ggplot(data_ab100, aes('x', fill='cat'))
    p + geom_point(aes(y='y', color='cat'), size=3, alpha=0.8) + \
        ggtitle('Scatter plot')
    return (p,)


@app.cell
def _(geom_histogram, ggtitle, p):
    p + geom_histogram() + ggtitle('Default histogram')
    return


@app.cell
def _(geom_histogram, ggtitle, p):
    p + geom_histogram(alpha=0.5, position='identity') + \
        ggtitle('Overlaid semi transparent histogram')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
