from dash import html
import dash_bootstrap_components as dbc

top_gdp_card = (
    dbc.Card(
        dbc.CardBody(
            [
                html.H4("Top GDP", className="card-title"),
                html.Iframe(
                    id="top-gdp-plot",
                    style={"border-width": "0", "width": "100%", "height": "250px"},
                ),
            ]
        ),
        className="col-md-4 mt-3",
    ),
)
