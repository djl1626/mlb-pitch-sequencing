"""
Functions used to get a pitcher's summary statistics
"""

import pandas as pd


def getPitchUsage(data: pd.DataFrame):
    summary_data = (data.groupby('pitch_type')['game_date']
                    .count()
                    .reset_index()
                    .rename(columns={'game_date': 'count_pitch_thrown'}))
    summary_data['percentage_pitch_thrown'] = (summary_data['count_pitch_thrown'] /
                                               sum(summary_data['count_pitch_thrown']))
    return summary_data
