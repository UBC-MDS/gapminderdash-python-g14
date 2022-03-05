from dash import Dash, Input, Output, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.queries import (
    get_labels_countries_in_continent_code,
)

from src.plotting import (
    plot_gdp_exp,
    plot_topGdp,
    plot_countries_kpis,
    plot_continent_kpis,
)

from src.component_app_header import app_header
from src.component_countries_kpis import countries_kpi_cards_div
from src.component_gdp_lifeexp import gdp_exp_card
from src.component_topgdp import top_gdp_card
from src.component_continent_kpis import continent_kpi_cards

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Div(
            [
                dbc.Row(app_header),  # row 1: app header
                dbc.Row(  # row 2: country kpis and ...
                    [
                        dbc.Col(countries_kpi_cards_div, width=6),
                        dbc.Col(continent_kpi_cards, width=6),
                    ]
                ),
                dbc.Row(  # row 3: continent kpis and ...
                    [
                        dbc.Col(gdp_exp_card, width=6),
                        dbc.Col(top_gdp_card, width=6),
                    ]
                ),
            ]
        )
    ],
    style={"padding": "5px 5px"},
)

# example of country dropdown options being updated based on selected continent
@app.callback(
    Output("country-selector", "options"),
    Input("continent-selector", "value"),
)
def update_country_dd_options(continent_code):
    return get_labels_countries_in_continent_code(continent_code)


# Update GDP vs Life Expectancy plot
@app.callback(
    Output(component_id="gdp-exp-plot", component_property="srcDoc"),
    [
        Input(component_id="continent-selector", component_property="value"),
        Input(component_id="country-selector", component_property="value"),
    ],
)
def update_gdp_exp_component(selected_continent, selected_countries):
    return plot_gdp_exp(selected_continent, selected_countries)


# Update Top GDP plot
@app.callback(
    Output(component_id="top-gdp-plot", component_property="srcDoc"),
    [
        Input(component_id="continent-selector", component_property="value"),
        Input(component_id="country-selector", component_property="value"),
    ],
)
def update_gdp_exp_component(selected_continent, selected_countries):
    return plot_topGdp(selected_continent, selected_countries)


# Update Country KPIs
@app.callback(
    [
        Output(component_id="gdp_country", component_property="children"),
        Output(component_id="pop_country", component_property="children"),
        Output(component_id="lifeexp_country", component_property="children"),
        Output(component_id="gdp_value", component_property="children"),
        Output(component_id="pop_value", component_property="children"),
        Output(component_id="lifeexp_value", component_property="children"),
    ],
    [
        Input(component_id="continent-selector", component_property="value"),
        Input(component_id="country-selector", component_property="value"),
        Input(component_id="country-kpi-type", component_property="value"),
    ],
)
def update_country_kpis(selected_continent, selected_countries, country_kpi_type):
    return plot_countries_kpis(selected_continent, selected_countries, country_kpi_type)


# Update Continent KPIs
@app.callback(
    [
        Output(component_id="continent-mean-gdp", component_property="children"),
        Output(component_id="continent-mean-pop", component_property="children"),
        Output(component_id="continent-mean-lifeexp", component_property="children"),
    ],
    [
        Input(component_id="continent-selector", component_property="value"),
        Input(component_id="country-selector", component_property="value"),
    ],
)
def update_continent_kpis(selected_continent, selected_countries):
    return plot_continent_kpis(selected_continent, selected_countries)


if __name__ == "__main__":
    app.run_server()
