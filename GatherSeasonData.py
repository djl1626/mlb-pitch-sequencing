"""
Gathers all Statcast data from 2023 MLB season.
"""

from pybaseball import statcast
import pandas as pd

# data = statcast(start_dt='2023-03-30', end_dt='2023-11-03')
# data.to_csv('/Data/2023StatcastData.csv')

statcast2023data = pd.read_csv("Data/2023StatcastData.csv")
playeriddata = pd.read_csv("Data/SFBB Player ID Map - PLAYERIDMAP.csv")

playeriddata = playeriddata[['FIRSTNAME', 'LASTNAME', 'IDFANGRAPHS', 'MLBID']]
playeriddata['full_name'] = playeriddata['FIRSTNAME'] + " " + playeriddata['LASTNAME']

statcast2023datawithnames = (pd.merge(statcast2023data, playeriddata, left_on='pitcher', right_on='MLBID')
                             .rename(columns={'FIRSTNAME': 'pitcher_first_name',
                                              'LASTNAME': 'pitcher_last_name',
                                              'IDFANGRAPHS': 'pitcher_fangraphs_id',
                                              'full_name': 'pitcher_full_name'})
                             .drop(columns=['MLBID'], axis=1))
statcast2023datawithnames = (pd.merge(statcast2023datawithnames, playeriddata, left_on='batter', right_on='MLBID')
                             .rename(columns={'FIRSTNAME': 'batter_first_name',
                                              'LASTNAME': 'batter_last_name',
                                              'IDFANGRAPHS': 'batter_fangraphs_id',
                                              'full_name': 'batter_full_name'})
                             .drop(columns=['MLBID'], axis=1))
statcast2023datawithnames.to_csv("Data/2023StatcastDataWithPlayerNames.csv")
