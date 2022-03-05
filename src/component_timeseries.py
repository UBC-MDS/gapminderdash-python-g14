from dash import html
import dash_bootstrap_components as dbc


timeseries-buttons = html.Div(
            [
                dbc.RadioItems(
                    id="timeseries-col",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "GDP", "value": 'gdpPercap'},
                        {"label": "Life Expectancy", "value": 'lifeExp'}
                    ],
                    value='gdpPercap',
                )
            ],
            className="radio-group col-md-4 mt-3",
        )


timeseries-card = 
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("Timeseries", className="card-title", id='timeseries-title'),
                    html.Iframe(
                        id="timeseries-plot",
                        style={"border-width": "0", "width": "100%", "height": "350px"},
                    ),
                ]
            ),
            className="col-md-4 mt-3",
        )
