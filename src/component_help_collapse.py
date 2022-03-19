from dash import html
import dash_bootstrap_components as dbc

help_collapse = (
    dbc.Collapse(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        html.H5("Working with GapminderDash"),
                    ),
                    dbc.Row(
                        [
                            html.P("Selecting a continent: "),
                            html.P("Selecting a country: "),
                            html.P("Map: "),
                            html.P("Time series plot: "),
                            html.P("GDP vs Life Expectancy: "),
                            html.P("Top GDP: "),
                            html.P("Country KPIs: "),
                            html.P("Continent KPIs: "),
                        ]
                    ),
                ]
            )
        ),
        id="help-collapse",
        is_open=False,
    ),
)
