# Surfs_Up

## Overview

The objective of this analysis is to support a business case for an investment in a Surf Board and Ice Cream shop on the Hawaiian Isalnd of Oahu.  The key investor has had prior bad experience opening a surf shop where rainy weather was an adverse factor.  To ensure that this new venture does not meet the same fate, he has asked for a weather analysis.


## Purpose

The purpose of the weather analysis is to examine weather patterns starting with temperature.  

A weather dataset was provided that contained observations of temperature and weather over the course of 8 years from 2010 through 2017 at 9 different weather stations on the island.


In order to understand temperature variation, data points were taken from the months of June and December 

The tools used for this analysis included Jupyter notebook, Pandas, Python, SQL Lite, and SQL Alchemy.  In addition, while not included in this report, Flask was used to develop a prototype app to share info in real time.  

Following is an example of the code used to extract temperatures from the month of June across all years in the dataset:

  ![GitHubLogo](https://github.com/rciminera/Surfs_Up/blob/main/extract_code.png)




Results:

Based on the temperature results of two months, Oahu is an ideal place for a Surf and Ice cream shop.  

1. The average temperature for June at 74.9 degrees and December at 71 degrees are warm enough for ice cream sales and for surfing. While December if 4 degrees cooler than June, the average temp is still warm enough for ice cream and surf shop sales.
2. The temperature variation in December while relatively low is still higher than June with a std deviation of 3.75 vs June at 3.25.  That being said, the low coefficients of variation (std/mean) for June and December are less than 1 which indicate that the temperatures are consistent during each month:  .04 for June and .05 for December
3. The minimum temperature in December is 56 degrees and less than 69 degrees 25% of the time versus June at 64 degrees and less than 73 degrees 25% of the time.  There will be some cool periods during December that may impact sales and the shop should look at measures to address this such as renting wet suits and adjusting hours of operation.

  ![GitHubLogo](https://github.com/rciminera/Surfs_Up/blob/main/June_temp_stats.png) ![GitHubLogo](thttps://github.com/rciminera/Surfs_Up/blob/main/Dec_temp_stats.png)


To refine this analyis there are at least three additional queries that should be provided for June and December:

1. Statistical analysis of precipitation for each month (see examples below)

2. Statistical analysis of precipitation and temperature by weather station to identify location differences and the optimal location for the shop.

3. A time of day view for each month to understand what might be the best hours of operation.

Example of precipitation analysis:

  ![GitHubLogo](https://github.com/rciminera/Surfs_Up/blob/main/June_rain.png) ![GitHubLogo](https://github.com/rciminera/Surfs_Up/blob/main/Dec_rain.png)