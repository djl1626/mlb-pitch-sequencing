"""
Functions to slice Statcast data into smaller datasets for small scale testing.
"""

import pandas as pd
from pybaseball import playerid_lookup, teamid_lookup


def writeToCSV(data: pd.DataFrame, file_path: str):
    if not file_path:
        file_path = "Data/"
    data.to_csv(file_path)


def getDataForTeam(data: pd.DataFrame, team: str, write_csv: bool, file_path: str):
    data = data[(data['home_team'] == team) | (data['away_team'] == team)]
    if write_csv:
        writeToCSV(data, file_path)
    return data


def getDataForPitcher(data: pd.DataFrame, pitcher: str, write_csv: bool, file_path: str):
    pitcher = pitcher.split(',')
    last = pitcher[0]
    first = pitcher[1]
    pitcher = playerid_lookup(last, first)
    data = data[data['pitcher'] == pitcher]
    if write_csv:
        writeToCSV(data, file_path)
    return data
