from dash import html, dcc
import dash_bootstrap_components as dbc
from src.queries import (
    get_labels_countries_in_continent_code,
    get_continent_labels,
)

from src.plotting import plot_countries_kpis, plot_gdp_exp, plot_topGdp

app_header = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                html.H3("Gapminder Dashboard", style={"font-size": "24px"}),
                width=3,
                style={"color": "white"},
            ),
            dbc.Col(
                dcc.Dropdown(
                    id="continent-selector",
                    value="All",
                    options=get_continent_labels(),
                ),
                width=4,
            ),
            dbc.Col(
                dcc.Dropdown(
                    id="country-selector",
                    options=get_labels_countries_in_continent_code(),
                    multi=True,
                ),
                width=5,
            ),
        ]
    ),
    className="p-3",
    style={"background-color": "black"},
    fluid=True,
)
