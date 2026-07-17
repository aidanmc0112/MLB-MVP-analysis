# MLB-MVP-analysis
Without using Fangraphs/Baseball Reference advanced metrics, how accurately can we predict the vote recipients for the Most Valuable Player Award?
# MLB MVP Prediction Model

## Overview

This project uses the Lahman Baseball Database and machine learning to predict Major League Baseball Most Valuable Player (MVP) voting. Rather than predicting only the winner, the model estimates each player's MVP vote share based on their offensive production, team success, defensive information, and league-relative performance.

The project is designed to recreate historical MVP voting patterns and evaluate how well player statistics explain MVP outcomes.

---

## Features

* Historical player statistics from the Lahman Baseball Database
* Automated player-season dataset creation
* Advanced offensive metrics including:

  * Batting Average (AVG)
  * Slugging Percentage (SLG)
  * On-Base Plus Slugging (OPS)
  * Batting Average on Balls in Play (BABIP)
* Team context through total team wins
* Defensive information including primary position and fielding statistics
* League-relative percentile rankings for key offensive categories
* Random Forest regression model predicting MVP vote share
* Historical backtesting using previous MLB seasons

---

## Dataset

The project is built using the Lahman Baseball Database (1871–2025).

Primary tables used include:

* People
* Batting
* Teams
* Fielding
* AwardsSharePlayers

These tables are merged into a single player-season dataset for modeling.

---

## Project Structure

```text
lahmans_project/
│
├── analysis.py              # Main entry point
├── analysis_loading.py      # Loads Lahman datasets
├── new_metrics.py           # Calculates derived statistics and feature engineering
├── regression.py            # Trains and evaluates the machine learning model
│
├── data/
│   └── lahman_1871-2025_csv/
│
└── README.md
```

---

## Machine Learning Pipeline

1. Load Lahman database tables.
2. Aggregate player statistics by season.
3. Calculate advanced metrics (OPS, SLG, BABIP, AVG).
4. Merge team wins, player information, and fielding data.
5. Create league-relative ranking features.
6. Merge historical MVP vote shares.
7. Train a Random Forest Regressor using historical seasons.
8. Predict MVP vote share for the test season.
9. Rank players by predicted vote share.

---

## Features Used

Current model features include:

* Home Runs (HR)
* Runs (R)
* Runs Batted In (RBI)
* Hits (H)
* Walks (BB)
* Strikeouts (SO)
* Stolen Bases (SB)
* Batting Average (AVG)
* Slugging Percentage (SLG)
* OPS
* BABIP
* Team Wins
* At Bats (AB)
* Fielding statistics
* Primary Position
* League-relative rankings:

  * HR Rank
  * RBI Rank
  * OPS Rank
  * SLG Rank

---

## Model

The current implementation uses a Random Forest Regressor from scikit-learn.

Target variable:

* MVP Vote Share

The model predicts a continuous vote share rather than simply classifying whether a player won the MVP award.

---

## Results

The model successfully identifies many of the top MVP candidates in recent seasons, including players such as Aaron Judge, Shohei Ohtani, and Cal Raleigh.

Feature importance analysis indicates that league-relative offensive performance is more predictive of MVP voting than raw counting statistics. Metrics such as RBI rank, OPS rank, and slugging percentage rank consistently rank among the most influential features.

---

## Current Limitations

Several factors that influence MVP voting are not available in the Lahman database:

* Wins Above Replacement (WAR)
* Defensive Runs Saved (DRS)
* Outs Above Average (OAA)
* Park-adjusted offensive metrics (wRC+, OPS+)
* Game-by-game or monthly performance trends
* Narrative factors considered by MVP voters

Because of these limitations, the model relies on traditional statistics and engineered features to approximate player value.

---

## Future Improvements

Potential enhancements include:

* Incorporating advanced metrics such as WAR and wRC+
* improving fielding metrics
* Experimenting with XGBoost and LightGBM
* Hyperparameter optimization
* Cross-validation across multiple historical seasons
* SHAP analysis for model interpretability
* Interactive visualizations of MVP predictions and feature importance

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook
* Visual Studio Code

---

## Running the Project

1. Download the Lahman Baseball Database and place the CSV files in the `data` directory.
2. Install the required Python packages:

```bash
pip install pandas numpy scikit-learn
```

3. Run the project:

```bash
python analysis.py
```

The program will build the player-season dataset, train the Random Forest model, and output predicted MVP vote shares for the selected test season.

---

## Author

Aidan McLaughlin

