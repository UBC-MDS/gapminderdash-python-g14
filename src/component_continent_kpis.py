from dash import html
import dash_bootstrap_components as dbc

continent_kpi_cards = dbc.Card(
    [
        dbc.CardHeader([html.H4("Continent Key Stats", className="card-title")]),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5(
                                                children="GDP",
                                                className="card-title",
                                                style={
                                                    "font-size": "32px",
                                                    "font-weight": "lighter",
                                                    "text-align": "center",
                                                },
                                            ),
                                            html.H5(
                                                children="mean",
                                                className="card-title",
                                                style={
                                                    "font-size": "16px",
                                                    "font-weight": "lighter",
                                                    "text-align": "center",
                                                },
                                            ),
                                            html.P(
                                                id="continent-mean-gdp",
                                                children="-",
                                                className="card-text",
                                                style={
                                                    "font-size": "24px",
                                                    "font-weight": "bold",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ]
                                    ),
                                ],
                                color="primary",
                                inverse=True,
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5(
                                                children="Population",
                                                className="card-title",
                                                style={
                                                    "font-size": "32px",
                                                    "font-weight": "lighter",
                                                    "text-align": "center",
                                                },
                                            ),
                                            html.H5(
                                                children="mean",
                                                className="card-title",
                                                style={
                                                    "font-size": "16px",
                                                    "font-weight": "lighter",
                                                    "text-align": "center",
                                                },
                                            ),
                                            html.P(
                                                id="continent-mean-pop",
                                                children="-",
                                                className="card-text",
                                                style={
                                                    "font-size": "24px",
                                                    "font-weight": "bold",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ]
                                    ),
                                ],
                                color="info",
                                inverse=True,
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5(
                                                children="Life Expectancy",
                                                className="card-title",
                                                style={
                                                    "font-size": "32px",
                                                    "font-weight": "lighter",
                                                    "text-align": "center",
                                                },
                                            ),
                                            html.H5(
                                                children="mean",
                                                className="card-title",
                                                style={
                                                    "font-size": "16px",
                                                    "font-weight": "lighter",
                                                    "text-align": "center",
                                                },
                                            ),
                                            html.P(
                                                id="continent-mean-lifeexp",
                                                children="-",
                                                className="card-text",
                                                style={
                                                    "font-size": "24px",
                                                    "font-weight": "bold",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ]
                                    ),
                                ],
                                color="secondary",
                                inverse=True,
                            )
                        ),
                    ]
                ),
            ]
        ),
    ]
)
