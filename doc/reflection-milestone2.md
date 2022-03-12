# Milestone 2 Reflection

## Dashboard Layout

The basic layout of our dashboard consists of 2 drop down menu options, 6 dash component cards and 4 different plots that summarize the metrics for the selected continents and countries. The 3 dash component cards on the left display the countries corresponding to the highest/lowest (selected by the user) GDP, population and life expectancy for the input continent. The remaining 3 dash component cards on the right provide the average value of the key statistics for the selected continent. Next, we have a plot for the high level view of the world map which highlights the continent selected from the drop down menu. The chart is useful to visualize and place the selected region on the map and generate insights from its key performance indicators. Below the map, we have a bubble chart to represent the correlation between GDP and life expectancy for the input region. The bubbles on the graph vary by the population of the input variables which is useful in inferring about socioeconomic standing of the selected country/continent. In addition to a country /continent specific plot, we have included a bar chart that displays the top 10 countries of the selected continent in order of their GDP per capita. The horizontal bars are highlighted based on the countries selected for a country specific analysis. Finally, we have a time series plot for the GDP and life expectancy over the years. The plot is flexible in terms of its input and is updated based on input country, continent and metric.


## Limitations

While the dashboard is an extremely useful tool to conduct a nation-wide analysis on performance indicators (GDP, life expectancy, population), it still has scope for improvement. Due to the time constraints, we were only able to implement key attributes of our dashboard with limited functionality. To begin with, the world map does not have a default view and is specific to the selected continent. It is not interactive with the countries selected and only highlights the selected continent. The summary statistics for the input countries is only for the latest year of the dataset (2007). Moreover, the axes labels for a few plots could be more human readable.


## Future Improvement

Based on our initial dashboard sketch, we plan to incorporate a help bar that documents the information contained by the plots and how to operate the filters. NExt, we can make the world map adapt to the input countries to make it more informative. In addition, the structure of the dashboard could be made more streamlined for users to access important information easily. It would also be useful to explore the possibility of linking plots based on user input to shift focus on selected countries/continent.
