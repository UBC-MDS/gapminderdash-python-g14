[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-dash-proj-g14

Welcome to our Gapminder dashboard project for DSCI 532!

The deployed version of the app can be found [here](https://gapdash14.herokuapp.com/):

## App Description

The main objective of this project is to build a Python application using Dash, that visualizes key performance indicators of the [Gapminder dataset](https://www.gapminder.org/data/). Users can leverage the dashboard to examine trends exhibited by the socioeconomic metrics of the dataset across countries and/or continents over a specified time range.

The app summarizes crucial information of the Gapminder dataset through illustrative plots that visualize the distribution of the dataset variables. The interface is designed to be interactive to make the app adaptive to the user input.

The default view of the dashboard is comprised of a chloropleth map (which discloses the country on hover), a time series plot, a scatterplot, a bar chart and a summary table. In addition, the landing page also displays high level summary statistics such as the highest and lowest GDP per capita, population and life expectancy for the default selection. To further analyze the features of our data, the dashboard offers filters in the form of drop-down lists and tabs to draw meaningful insights specific to a particular continent, country, year or metric (Life expectancy, GDP per capita). Users can also analyze the global standing of countries in their continent (given by a continental summary table) and review top 5 countries for the selected metric and time range (in a bar chart).

The dashboard can be of significant use for consumers who wish to identify systematic misconceptions about important global trends/ proportions and examine how they evolved over the years.

## Usage

A basic overview of the dashboard is as follows:

-   The app can be run from the terminal as described in the installation section
-   The landing page shows data for all continents by default.
-   Select the desired continent and/or countries to analyze their performance in terms of key performance indicators (GDP, life expectancy and population)
-   The time series plot also lets the user select the metric (GDP or life expectancy) to review trends exhibited by those measures across the years based on the input selection.

A help panel is available on the dashboard and can be accessed by clicking the 'Help' button. Here, users will find details about the charts available on the dashboard. 

<img width="800" alt="pythondash-helppanel-milestone4" src="https://user-images.githubusercontent.com/75291170/159138122-168a2e12-fc52-4553-b6f2-6668dbe0d692.PNG">

## Proposed Dashboard Layout

<img width="800" alt="pythondash-milestone4" src="https://user-images.githubusercontent.com/75291170/159137867-5e8584ff-8ec8-480d-99cc-ad55be7618bb.PNG">

## Contributions

Contributors: 

- Amir Abbas Shojakhani
- Luke Collins 
- Sukhleen Kaur

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing document](https://github.com/UBC-MDS/gapminderdash-python-g14/blob/feat-map/CONTRIBUTING.md).

## Installation

If you would like to help contribute to the app, you can set up the system as follows:

1.  Download the necessary packages listed in `requirements.txt` using `pip` or `conda`

2.  Clone this repo using [`https://github.com/UBC-MDS/gapminderdash-python-g14`](https://github.com/UBC-MDS/gapminderdash-python-g14.git)

To run the app locally:

1.  Navigate to the root of this repo

2.  In the command line, enter:

```bash
python app.py
```

3.  Copy the address printed out after "Dash is running on" to a browser to view the Dash app.

### Run the app locally

To run this app using Docker write the following commands after cloning the repo:

``` bash
cd gapminderdash-python-g14
docker-compose up
```

Finally, open the app in the following URL <http://localhost:8000/>

## License

`python-dash-proj-g14` was created by Amir Abbas Shojakhani, Luke Collins and Sukhleen Kaur. It is licensed under the terms of the MIT license.
