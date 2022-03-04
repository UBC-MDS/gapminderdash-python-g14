from dash import html
import dash_bootstrap_components as dbc

gdp_exp_card = (
    dbc.Card(
        dbc.CardBody(
            [
                html.H4("GDP vs Life Expectancy", className="card-title"),
                html.Iframe(
                    id="variables-comparisons-plot",
                    style={"border-width": "0", "width": "100%", "height": "300px"},
                ),
            ]
        ),
        className="col-md-4 mt-3",
    ),
)
