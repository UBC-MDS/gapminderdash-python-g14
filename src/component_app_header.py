from dash import html, dcc
import dash_bootstrap_components as dbc
from src.queries import (
    get_labels_countries_in_continent_code,
    get_continent_labels,
)

from src.plotting import plot_countries_kpis, plot_gdp_exp, plot_topGdp

app_header = [
    dbc.Col(html.H3("Gapminder Dashboard")),
    dbc.Col(
        dcc.Dropdown(
            id="continent-selector",
            value="All",
            # style={"width": "50%"},
            options=get_continent_labels(),
        )
    ),
    dbc.Col(
        dcc.Dropdown(
            id="country-selector",
            value=["All"],
            options=get_labels_countries_in_continent_code(),
            multi=True,
            # style={"width": "50%"},
        )
    ),
]
