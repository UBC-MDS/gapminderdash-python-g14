from dash import html
import dash_bootstrap_components as dbc
from src.plotting import plot_topGdp

top_gdp_card = [
    dbc.Card(
        [
            dbc.CardHeader(html.H4("Top GDP", className="card-title")),
            dbc.CardBody(
                [
                    html.Iframe(
                        id="top-gdp-plot",
                        srcDoc=plot_topGdp(),
                        style={"border-width": "0", "width": "100%", "height": "250px"},
                    ),
                ]
            ),
        ]
    ),
]
