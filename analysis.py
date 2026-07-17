batting_season = (
    batting.groupby(["playerID", "yearID"])
    .agg({
        "AB":"sum",
        "H":"sum",
        "HR":"sum",
        "R":"sum",
        "RBI":"sum",
        "BB":"sum",
        "SO":"sum",
        "SB":"sum",
        "BA":"sum",
        "BABIP":"mean",
        "SLG":"mean",
        "OPS":"mean"
    })
    .reset_index()
)
batting_season = batting_season.merge(
    people[["playerID","nameFirst","nameLast"]],
    on="playerID",
    how="left"
)
batting_season = batting_season.merge(
    primary_pos,
    on=["playerID", "yearID"],
    how="left"
)
# Get the final team a player played for in each season

player_team = (
    batting
    .sort_values(["playerID", "yearID"])
    .groupby(["playerID", "yearID"])
    .tail(1)
)
player_team = player_team.merge(
    teams[[
        "yearID",
        "teamID",
        "lgID",
        "W"
    ]],
    on=["yearID","teamID","lgID"],
    how="left"
)
batting_season = batting_season.merge(
    player_team[
        [
            "playerID",
            "yearID",
            "lgID",
            "W"
        ]
    ],
    on=["playerID", "yearID"],
    how="left",
    suffixes=("", "_team")
)
if "lgID_team" in batting_season.columns:
    batting_season = batting_season.drop(columns=["lgID_team"])

# Remove duplicate fielding columns if they already exist
fielding_cols = [
    "G_x", "InnOuts_x", "A_x", "E_x", "PO_x", "POS_x",
    "G_y", "InnOuts_y", "A_y", "E_y", "PO_y", "POS_y"
]

batting_season = batting_season.drop(
    columns=[col for col in fielding_cols if col in batting_season.columns]
)

fielding_season = (
    fielding.groupby(["playerID", "yearID"])
    .agg({
        "G": "sum",
        "InnOuts": "sum",
        "PO": "sum",
        "A": "sum",
        "E": "sum",
        "Chances": "sum"
    })
    .reset_index()
)

fielding_season["FieldingPct"] = np.where(
    fielding_season["Chances"] > 0,
    (fielding_season["PO"] + fielding_season["A"]) /
    fielding_season["Chances"],
    np.nan
)

fielding_season["ErrorRate"] = np.where(
    fielding_season["Chances"] > 0,
    fielding_season["E"] /
    fielding_season["Chances"],
    np.nan
)
# Merge fielding stats
batting_season = batting_season.merge(
    fielding_season,
    on=["playerID", "yearID"],
    how="left"
)
# Fix duplicate league columns
if "lgID_x" in batting_season.columns and "lgID_y" in batting_season.columns:
    batting_season["lgID"] = batting_season["lgID_y"]
    batting_season = batting_season.drop(
        columns=["lgID_x", "lgID_y"]
    )

mvp = awards[
    awards["awardID"]=="Most Valuable Player"
].copy()



mvp["VoteShare"] = (
    mvp["pointsWon"] /
    mvp["pointsMax"]
)



mvp = mvp[
    [
        "playerID",
        "yearID",
        "VoteShare"
    ]
]



full_data = batting_season.merge(
    mvp,
    on=["playerID","yearID"],
    how="left"
)
full_data["VoteShare"] = (
    full_data["VoteShare"]
    .fillna(0)
)
full_data = pd.get_dummies(
    full_data,
    columns=["POS"],
    prefix="POS"
)
full_data["HR_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["HR"]
    .rank(pct=True)
)

full_data["OPS_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["OPS"]
    .rank(pct=True)
)

full_data["RBI_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["RBI"]
    .rank(pct=True)
)
full_data["SLG_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["SLG"]
    .rank(pct=True)
)
full_data["BA_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["BA"]
    .rank(pct=True)
)
full_data["R_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["R"]
    .rank(pct=True)
)
full_data["H_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["H"]
    .rank(pct=True)
)
full_data["BB_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["BB"]
    .rank(pct=True)
)
full_data["SB_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["SB"]
    .rank(pct=True)
)
full_data["SO_rank"] = (
    full_data
    .groupby(["yearID", "lgID"])["SO"]
    .rank(pct=True)
)
full_data = full_data[
    (
        
        (full_data["AB"] >= 300)
    )
]
train = full_data[
    (full_data["yearID"] < 2025) &
    (full_data["yearID"] != 2020)
].copy()


test = full_data[
    full_data["yearID"] == 2025
].copy()
position_features = [
    col for col in full_data.columns
    if col.startswith("POS_")
]
features = [
    "HR",
    "R",
    "RBI",
    "H",
    "BB",
    "SO",
    "SB",
    "OPS",
    "SLG",
    "OPS_rank",
    "HR_rank",
    "RBI_rank",
    "SLG_rank",
    "SO_rank",
    "BA_rank",
    "BB_rank",
    "R_rank",
    "H_rank",
    "SB_rank",
    "BA",
    "BABIP",
    "W",
    "AB",
    "E",
    "FieldingPct",
    "ErrorRate",
    "Chances"
] + position_features
X_train = train[features].fillna(0)
y_train = train["VoteShare"]

X_test = test[features].fillna(0)
y_test = test["VoteShare"]
