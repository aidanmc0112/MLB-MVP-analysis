import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
def load_data():
  path = r""
  
  batting = pd.read_csv(path + r"\Batting.csv")
  people = pd.read_csv(path + r"\People.csv")
  teams = pd.read_csv(path + r"\Teams.csv")
  awards = pd.read_csv(path + r"\AwardsSharePlayers.csv")
  fielding = pd.read_csv(path + r"\Fielding.csv")
  return people, batting, teams, fielding, awards
