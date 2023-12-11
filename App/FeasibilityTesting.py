from Functions import PitcherStatistics, StatcastSlicer
import pandas as pd

# statcast_data_2023 = pd.read_csv("/Users/djl47/PycharmProjects/BaseballDS/mlb-pitch-sequencing/Data/2023StatcastData.csv")
# red_sox_data_2023 = StatcastSlicer.getDataForTeam(statcast_data_2023, 'BOS', write_csv=True, file_path="/Users/djl47/PycharmProjects/BaseballDS/mlb-pitch-sequencing/Data/2023RedSoxData.csv")
#
# red_sox_data_2023 = pd.read_csv("Data/2023RedSoxData.csv")
# brayan_bello_data_2023 = red_sox_data_2023[red_sox_data_2023['pitcher'] == 678394]
# brayan_bello_data_2023.to_csv("/Users/djl47/PycharmProjects/BaseballDS/mlb-pitch-sequencing/Data/BrayanBello2023Data.csv")

# brayan_bello = pd.read_csv("/Users/djl47/PycharmProjects/BaseballDS/mlb-pitch-sequencing/Data/BrayanBello2023Data.csv")
# summary_data = PitcherStatistics.getPitchUsage(brayan_bello_data_2023)

red_sox_data_2023 = pd.read_csv("/Users/djl47/PycharmProjects/BaseballDS/mlb-pitch-sequencing/Data/2023RedSoxData.csv")
summary_data = PitcherStatistics.getPitchUsage(red_sox_data_2023)
