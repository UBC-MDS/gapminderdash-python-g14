from dash import html
import dash_bootstrap_components as dbc

map_card = (
    dbc.Card(
        dbc.CardBody(
            [
                html.H4("Map", className="card-title"),
                html.Iframe(
                    id="map",
                    style={"border-width": "0", "width": "100%", "height": "300px"},
                ),
            ]
        ),
        className="mt-3 mb-3",
    ),
)
