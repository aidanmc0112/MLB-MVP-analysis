import pandas as pd
import numpy as np

path = r"C:\Users\aidan\Downloads\lahmans_project\data\lahman_1871-2025_csv"

batting = pd.read_csv(path + r"\Batting.csv")
people = pd.read_csv(path + r"\People.csv")
teams = pd.read_csv(path + r"\Teams.csv")
awards = pd.read_csv(path + r"\AwardsSharePlayers.csv")
fielding = pd.read_csv(path + r"\Fielding.csv")
