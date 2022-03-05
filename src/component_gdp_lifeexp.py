from dash import html
import dash_bootstrap_components as dbc
from src.plotting import plot_gdp_exp

gdp_exp_card = [
    dbc.Card(
        [
            dbc.CardHeader(html.H4("GDP vs Life Expectancy", className="card-title")),
            dbc.CardBody(
                [
                    html.Iframe(
                        id="gdp-exp-plot",
                        srcDoc=plot_gdp_exp(),
                        style={"border-width": "0", "width": "100%", "height": "300px"},
                    ),
                ]
            ),
        ]
    ),
]
