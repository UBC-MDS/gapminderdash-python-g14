def get_labels_countries_in_continent_code(continent_code="All"):
    all_label = [{"label": "All countries", "value": "All"}]
    if continent_code == "All":
        return all_label + [
            {"label": x[0], "value": x[1]}
            for x in dp.transformed_raw_data.loc[:, ["Country", "country_code"]]
            .drop_duplicates()
            .values
        ]
    else:
        return all_label + [
            {"label": x[0], "value": x[1]}
            for x in dp.transformed_raw_data.loc[:, ["Country", "country_code"]]
            .loc[dp.transformed_raw_data["continent_code"] == continent_code]
            .drop_duplicates()
            .values
        ]


def get_labels_continent_with_country_code(country_code="All"):
    all_label = [{"label": "All continents", "value": "All"}]
    if country_code == "All":
        return all_label + [
            {"label": x[0], "value": x[1]}
            for x in dp.transformed_raw_data.loc[:, ["Continent", "continent_code"]]
            .drop_duplicates()
            .values
        ]
    else:
        return all_label + [
            {"label": x[0], "value": x[1]}
            for x in dp.transformed_raw_data.loc[:, ["Continent", "continent_code"]]
            .loc[dp.transformed_raw_data["country_code"] == country_code]
            .drop_duplicates()
            .values
        ]


def get_labels_continent_with_continent_code(continent_code="All"):
    prefix = "Continental Summary - {}"
    if continent_code != "All":
        continents = dp.transformed_raw_data.loc[
            :, ["Continent", "continent_code"]
        ].drop_duplicates()
        label = continents.loc[continents["continent_code"] == continent_code][
            "Continent"
        ].values[0]
    else:
        label = "All continents"

    return prefix.format(label)
