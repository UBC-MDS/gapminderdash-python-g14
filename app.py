from dash import Dash, Input, Output, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.queries import (
    get_labels_countries_in_continent_code,
    get_continent_labels,
)

from src.plotting import plot_gdp_exp, plot_topGdp

from src.component_app_header import app_header
from src.component_countries_kpis import countries_kpi_cards_div
from src.component_gdp_lifeexp import gdp_exp_card
from src.component_topgdp import top_gdp_card

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Div(
            [
                dbc.Row(app_header),  # row 1: app header
                dbc.Row(  # row 2: country kpis and ...
                    [dbc.Col(countries_kpi_cards_div, width=6)]
                ),
                dbc.Row(  # row 3: some other stuff
                    [
                        dbc.Col(gdp_exp_card, width=4),
                        dbc.Col(top_gdp_card, width=4),
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
    print(selected_countries)
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
    print(selected_countries)
    return plot_topGdp(selected_continent, selected_countries)


if __name__ == "__main__":
    app.run_server()
