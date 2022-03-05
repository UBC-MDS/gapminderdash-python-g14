import altair as alt
from src.queries import get_continent_data_filtered_year
import pandas as pd


def plot_continent_kpis(selected_continent="All", selected_countries=None):
    kpi_data = get_continent_data_filtered_year(2007, selected_continent)
    if selected_continent == "All":
        continent_mean_gdp = kpi_data.mean()["gdpPercap"]
        continent_mean_pop = kpi_data.mean()["pop"]
        continent_mean_lifeexp = kpi_data.mean()["lifeExp"]
    else:
        continent_mean_gdp = kpi_data.groupby("continent").mean()["gdpPercap"]
        continent_mean_pop = kpi_data.groupby("continent").mean()["pop"]
        continent_mean_lifeexp = kpi_data.groupby("continent").mean()["lifeExp"]

    return (
        round(continent_mean_gdp, 2),
        round(continent_mean_pop, 2),
        round(continent_mean_lifeexp, 2),
    )


def plot_countries_kpis(
    selected_continent="All", selected_countries=None, country_kpi_type=1
):
    kpi_data = get_continent_data_filtered_year(2007, selected_continent)

    # Show highest or lowest based on user selection
    if country_kpi_type == 1:
        gdp_country = kpi_data.nlargest(1, columns="gdpPercap")["country"]
        pop_country = kpi_data.nlargest(1, columns="pop")["country"]
        lifeexp_country = kpi_data.nlargest(1, columns="lifeExp")["country"]
        gdp_value = kpi_data.nlargest(1, columns="gdpPercap")["gdpPercap"]
        pop_value = kpi_data.nlargest(1, columns="pop")["pop"]
        lifeexp_value = kpi_data.nlargest(1, columns="lifeExp")["lifeExp"]
    else:
        gdp_country = kpi_data.nsmallest(1, columns="gdpPercap")["country"]
        pop_country = kpi_data.nsmallest(1, columns="pop")["country"]
        lifeexp_country = kpi_data.nsmallest(1, columns="lifeExp")["country"]
        gdp_value = kpi_data.nsmallest(1, columns="gdpPercap")["gdpPercap"]
        pop_value = kpi_data.nsmallest(1, columns="pop")["pop"]
        lifeexp_value = kpi_data.nsmallest(1, columns="lifeExp")["lifeExp"]

    return (
        gdp_country,
        pop_country,
        lifeexp_country,
        gdp_value,
        pop_value,
        lifeexp_value,
    )


def plot_gdp_exp(selected_continent="All", selected_countries=None):
    plot_data = get_continent_data_filtered_year(2007, selected_continent).sort_values(
        "gdpPercap", ascending=False
    )

    # Add highlight column
    plot_data["highlight"] = False

    # If countries are selected
    if selected_countries != None:
        selected_countries_data = plot_data.query(
            "country in @selected_countries"
        ).sort_values("gdpPercap", ascending=False)
        plot_data = pd.concat(
            [plot_data, selected_countries_data], ignore_index=True
        ).sort_values("gdpPercap", ascending=False)

        # Change highlight to true for selected countries and drop duplicates
        plot_data["highlight"] = False
        plot_data.loc[
            plot_data["country"].isin(selected_countries), ["highlight"]
        ] = True
        plot_data.drop_duplicates(inplace=True)

    chart = (
        alt.Chart(plot_data)
        .mark_circle()
        .encode(
            x="lifeExp",
            y=alt.Y("gdpPercap", sort="-x"),
            color=alt.Color("highlight", legend=None),
            tooltip="country",
            size="pop",
        )
        .interactive()
        .configure_axis(grid=False)
        .configure_view(strokeWidth=0)
    ).properties(width=300, height=250)
    return chart.to_html()


def plot_topGdp(selected_continent="All", selected_countries=None):

    plot_data = get_continent_data_filtered_year(2007, selected_continent).sort_values(
        "gdpPercap", ascending=False
    )[:10]
    plot_data["highlight"] = False

    # If countries are selected
    if selected_countries != None:
        continent_data = get_continent_data_filtered_year(2007, selected_continent)
        selected_countries_data = continent_data.loc[
            continent_data["country"].isin(selected_countries)
        ].sort_values("gdpPercap", ascending=False)
        plot_data = pd.concat(
            [plot_data, selected_countries_data], ignore_index=True
        ).sort_values("gdpPercap", ascending=False)

        # Change highlight to true for selected countries and drop duplicates
        plot_data["highlight"] = False
        plot_data.loc[
            plot_data["country"].isin(selected_countries), ["highlight"]
        ] = True
        plot_data.drop_duplicates(inplace=True)

    print(plot_data)
    chart = (
        alt.Chart(plot_data)
        .mark_bar()
        .encode(
            x="gdpPercap",
            y=alt.Y("country", sort="-x"),
            color=alt.Color("highlight", legend=None),
        )
        .interactive()
        .configure_axis(grid=False)
        .configure_view(strokeWidth=0)
    ).properties(width=350, height=200)
    return chart.to_html()


cols = {'gdpPercap': 'GDP', 'lifeExp': 'Life Expectancy'}

def time_series_plot(df, ycol, all_continents=False):

    if not all_continents:
        chart = alt.Chart(df).  mark_line().encode(
            x=alt.X('year', title = 'Year', axis=alt.Axis(format='1000')),
            y=alt.Y(ycol, title = cols[ycol]),
            color = "country:O",
            tooltip=[ycol, 'year']).interactive()

    else:
        chart = alt.Chart(df).  mark_line(interpolate = "monotone").encode(
            x=alt.X('year', title = 'Year', axis=alt.Axis(format='1000')),
            y=alt.Y(ycol, title = cols[ycol]),
            color = "continent:O",
            tooltip=[ycol, 'year']).interactive()
    
    return chart.to_html()