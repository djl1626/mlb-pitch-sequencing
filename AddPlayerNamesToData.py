"""
Joins the Statcast data with player names and FanGraphs IDs.

Only joins the batter and pitcher names, but can easily be replicated to bring other player names into the main
dataframe.
"""

import pandas as pd

statcast2023data = pd.read_csv("Data/2023StatcastData.csv")
playeriddata = pd.read_csv("Data/SFBB Player ID Map - PLAYERIDMAP.csv")

playeriddata = playeriddata[['FIRSTNAME', 'LASTNAME', 'IDFANGRAPHS', 'MLBID']]
playeriddata['full_name'] = playeriddata['FIRSTNAME'] + " " + playeriddata['LASTNAME']

"""
Join the pitcher names
"""
statcast2023datawithnames = (pd.merge(statcast2023data, playeriddata, left_on='pitcher', right_on='MLBID')
                             .rename(columns={'FIRSTNAME': 'pitcher_first_name',
                                              'LASTNAME': 'pitcher_last_name',
                                              'IDFANGRAPHS': 'pitcher_fangraphs_id',
                                              'full_name': 'pitcher_full_name'})
                             .drop(columns=['MLBID'], axis=1))

"""
Join the batter names
"""
statcast2023datawithnames = (pd.merge(statcast2023datawithnames, playeriddata, left_on='batter', right_on='MLBID')
                             .rename(columns={'FIRSTNAME': 'batter_first_name',
                                              'LASTNAME': 'batter_last_name',
                                              'IDFANGRAPHS': 'batter_fangraphs_id',
                                              'full_name': 'batter_full_name'})
                             .drop(columns=['MLBID'], axis=1))

statcast2023datawithnames.to_csv("Data/2023StatcastDataWithPitcherBatterNames.csv")