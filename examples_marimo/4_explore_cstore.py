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
    return (pl,)


@app.cell
def _(pl):
    discounts = pl.read_parquet("../cstore/cstore_discounts.parquet")
    payments = pl.read_parquet("../cstore/cstore_payments.parquet")
    sets = pl.read_parquet("../cstore/cstore_transaction_sets.parquet")
    daily = pl.read_parquet("../cstore/cstore_transactions_daily_agg.parquet")
    items = pl.read_parquet("../cstore/pdi_cstore_transection_items.parquet")
    shopper = pl.read_parquet("../cstore/cstore_shopper.parquet")
    gtin = pl.read_parquet("../cstore/cstore_master_ctin.parquet")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""1. Which shoppers had the most transactions (shoppers)""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""2. spent the most money (payments) (null shoppers are removed)""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""3. bought the most bottles/cans of soda? (items, shoppers)""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""4. How do days of the week compare for the total transactions and total sales? (daily, monday = 1 and sunday = 7)""")
    return


@app.cell
def _():
    return


app._unparsable_cell(
    r"""
    5. How do the hours of 7 am to 11 am compare for weekdays and weekends when looking at total transactions? (sets)
    """,
    column=None, disabled=False, hide_code=True, name="_"
)


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
