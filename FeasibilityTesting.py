import pandas as pd
from StatcastSlicer import *
from PitcherStatistics import *

# statcast_data_2023 = pd.read_csv("Data/2023StatcastData.csv")
# red_sox_data_2023 = getDataForTeam(statcast_data_2023, 'BOS', write_csv=True, file_path="Data/2023RedSoxData.csv")

# red_sox_data_2023 = pd.read_csv("Data/2023RedSoxData.csv")
# brayan_bello_data_2023 = red_sox_data_2023[red_sox_data_2023['pitcher'] == 678394]
# brayan_bello_data_2023.to_csv("Data/BrayanBello2023Data.csv")

brayan_bello = pd.read_csv("Data/BrayanBello2023Data.csv")
summary_data = getPitchUsage(brayan_bello)
