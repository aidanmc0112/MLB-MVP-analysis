from analysis_loading import load_data
from new_metrics import create_metrics
from regression import run_regression

people, batting, teams, fielding, awards = load_data()

full_data = create_metrics(
    batting,
    teams,
    fielding,
    awards,
    people
)

model = run_regression(full_data)
