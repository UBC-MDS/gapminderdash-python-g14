from dash import html
import dash_bootstrap_components as dbc

countries_kpi_type_div = html.Div(
    [
        dbc.RadioItems(
            id="country-kpi-type",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Highest", "value": 1},
                {"label": "Lowest", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output-country-kpi"),
    ],
    className="radio-group col-md-4 mt-3",
)

countries_kpi_cards_div = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "GDP",
                                        className="card-title",
                                        style={
                                            "font-size": "18px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                    html.P(
                                        id="gdp_country",
                                        children="-",
                                        className="card-text",
                                        style={
                                            "font-size": "24px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                    html.P(
                                        id="gdp_value",
                                        children="-",
                                        className="card-text",
                                        style={
                                            "font-size": "14px",
                                        },
                                    ),
                                ]
                            ),
                        ],
                        color="success",
                        inverse=True,
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "Population",
                                        className="card-title",
                                        style={
                                            "font-size": "18px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                    html.P(
                                        id="pop_country",
                                        children="-",
                                        className="card-text",
                                        style={
                                            "font-size": "24px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                    html.P(
                                        id="pop_value",
                                        children="-",
                                        className="card-text",
                                        style={
                                            "font-size": "14px",
                                        },
                                    ),
                                ]
                            ),
                        ],
                        color="warning",
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
                                            "font-size": "18px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                    html.P(
                                        id="lifeexp_country",
                                        children="-",
                                        className="card-text",
                                        style={
                                            "font-size": "24px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                    html.P(
                                        id="lifeexp_value",
                                        children="-",
                                        className="card-text",
                                        style={
                                            "font-size": "14px",
                                        },
                                    ),
                                ]
                            ),
                        ],
                        color="danger",
                        inverse=True,
                    )
                ),
            ],
            className="mb-4",
        ),
    ]
)
