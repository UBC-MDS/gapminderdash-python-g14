import altair as alt

def plot_topGdp(selected_continent, selected_countries, country_kpi_type):
    kpi_data = gapminder_data.query(
        "(year == 2007) & (continent == @selected_continent)"
    )

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
    