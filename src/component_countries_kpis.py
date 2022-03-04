from dash import html
import dash_bootstrap_components as dbc

countries_kpi_type_div = [
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
    )
]

countries_kpi_cards_div = [
    dbc.Row(countries_kpi_type_div),
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
                ),
                width=4,
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
                ),
                width=4,
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
                ),
                width=4,
            ),
        ]
    ),
]
