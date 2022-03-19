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
                            html.P("Continent dropdown: Choose the continent from the dropdown menu that you wish to analyze. "),
                            html.P("Country dropdown: Select one or more countries for the chosen continent to review their statistics."),
                            html.P("Map: Represents the selected continent in the world map."),
                            html.P("Time series plot: Plots trends of the selected metric (GDP/Life Expectancy) over the years for the input continent/countries."),
                            html.P("GDP vs Life Expectancy: Visualizes the relationship between GDP and Life Expectancy by population for the chosen region."),
                            html.P("Top GDP: Gives the top 10 countries for highest GDP and highlights the selected countries, if any."),
                            html.P("Country KPIs: Prints the countries with Highest/Lowest GDP, Population and Life Expectancy based on the continent selected."),
                            html.P("Continent KPIs: Prints the average GDP, Population and Life Expectancy for the selected continent."),
                        ]
                    ),
                ]
            )
        ),
        id="help-collapse",
        is_open=False,
    ),
)
