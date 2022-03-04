from dash import html, dcc
from queries import (
    get_labels_countries_in_continent_code,
    get_continent_labels,
)

from plotting import plot_countries_kpis, plot_gdp_exp, plot_topGdp

app_header = [
    dcc.Dropdown(
        id="continent-selector",
        value="All",
        style={"width": "50%"},
        options=[get_continent_labels()],
    ),
    dcc.Dropdown(
        id="country-selector",
        value="All",
        options=[get_labels_countries_in_continent_code()],
        multi=True,
        style={"width": "50%"},
    ),
]
