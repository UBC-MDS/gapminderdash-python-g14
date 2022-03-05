from gapminder import gapminder

# Set global app variable gapminder_data
# so that we only need to instantiate this once

gapminder_data = gapminder


def get_labels_countries_in_continent_code(continent_code="All"):
    if continent_code == "All":
        return [
            {"label": country, "value": country}
            for country in gapminder_data["country"].unique()
        ]
    else:
        return [
            {"label": country, "value": country}
            for country in gapminder_data["country"]
            .loc[gapminder_data["continent"] == continent_code]
            .unique()
        ]


def get_continent_labels():
    all_label = [{"label": "All continents", "value": "All"}]
    return all_label + [
        {"label": col, "value": col} for col in gapminder_data["continent"].unique()
    ]


def get_continent_data_filtered_year(year, continent):
    if continent == "All":
        data = gapminder_data.query("year == @year")
    else:
        data = gapminder_data.query("(year == @year) & (continent == @continent)")
    return data
