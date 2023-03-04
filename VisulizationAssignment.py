# -*- coding: utf-8 -*-

# Student ID:   2231457
# Name:         Theepag Atputhalingam

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(data, title, xlabel=None, ylabel=None):
    ''' Function to create a line plot. Arguments:
        A dataframe with the needed coloumns
        title contains the title of the plot
        xlabel contains the name of x axis
        ylabel contains the name of y axis
    '''
    #Plotting line plot
    plt.figure()
    data.plot.line()

    #Title
    plt.title(title)

    #Labelling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend()

    # save as png image
    plt.savefig("linplot.png",  dpi=300, bbox_inches='tight')

    plt.show()
    return


def barplot(data, title, xlabel=None, ylabel=None):
    ''' Function to create a bar plot. Arguments:
        A dataframe with the needed coloumns
        title contains the title of the plot
        xlabel contains the name of x axis
        ylabel contains the name of y axis
    '''
    #selected countries to compare carbon emission
    countries = ['China', 'United Kingdom']

    #Lambda function to get 10 year interval
    df_co2_emission_china_uk = data[countries].iloc[lambda x: x.index % 10 == 0]

    #Plotting line plot
    plt.figure()
    df_co2_emission_china_uk.plot.bar()

    #Title
    plt.title(title)

    #Labelling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend()

    # save as png image
    plt.savefig("barplot.png",  dpi=300, bbox_inches='tight')

    plt.show()
    return


def pieplot(data, title, year, xlabel=None, ylabel=None):
    ''' Function to create a pie plot. Arguments:
        A dataframe with the needed coloumns
        title contains the title of the pie plot
        
        xlabel contains the name of x axis
        ylabel contains the name of y axis
        
    '''
    #selected countries to compare carbon emission
    countries = ['China', 'United States',
                 'India', 'Japan', 'Iran, Islamic Rep.']
    df_co2_emission_per_capita_countries = data[countries].loc[year]

    #Plotting pie plot
    plt.figure()
    df_co2_emission_per_capita_countries.plot.pie()
    print(df_co2_emission_per_capita_countries)

    #Title
    plt.title(title)

    #Labelling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # save as png image
    plt.savefig(f'{title}.png',  dpi=300, bbox_inches='tight')

    plt.show()


# Read UK average house price index dataset and set index column
df_avg_house_price = pd.read_csv(
    "avarage_house_price_in_the_UK.csv", index_col=0)

# Calling lineplot function to get average house price by country
lineplot(df_avg_house_price, "Average house price by country",
         "Time", "Average house price(GBP£)")

# Read CO2 emission per capita dataset and setting year as index column
df_co2_emission_per_capita = pd.read_csv(
    'CO2_Emissions_1960-2018.csv', index_col=0)

# Calling barplot function
barplot(df_co2_emission_per_capita, 'Carbon emission per capita',
        xlabel='Year', ylabel='CO2 emission per capita (t)')

#Calling pieplot function to compare pie chart of year 1960 and 2018
pieplot(df_co2_emission_per_capita, 'CO2 emissions in 1960', 1960)
pieplot(df_co2_emission_per_capita, 'CO2 emissions in 2018', 2018)
