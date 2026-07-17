# BABIP
sf = batting["SF"].fillna(0)
so = batting["SO"].fillna(0)

denom = batting["AB"] - batting["HR"] - so + sf

batting["BABIP"] = np.where(
    denom > 0,
    (batting["H"] - batting["HR"]) / denom,
    np.nan
)

batting["BA"] = np.where(
    batting["AB"] > 0,
    batting["H"] / batting["AB"],
    np.nan
)
# OBP
bb = batting["BB"].fillna(0)
hbp = batting["HBP"].fillna(0)

obp_denom = batting["AB"] + bb + hbp + sf

batting["OBP"] = np.where(
    obp_denom > 0,
    (batting["H"] + bb + hbp) / obp_denom,
    np.nan
)


# SLG
singles = (
    batting["H"]
    - batting["2B"]
    - batting["3B"]
    - batting["HR"]
)

total_bases = (
    singles
    + 2 * batting["2B"]
    + 3 * batting["3B"]
    + 4 * batting["HR"]
)

batting["SLG"] = np.where(
    batting["AB"] > 0,
    total_bases / batting["AB"],
    np.nan
)


# OPS
batting["OPS"] = batting["OBP"] + batting["SLG"]


#chances
fielding["Chances"] = (
    fielding["PO"] +
    fielding["A"] +
    fielding["E"]
)
#fielding pct
fielding["FieldingPct"] = (
    (fielding["PO"] + fielding["A"]) /
    (fielding["Chances"])
)
#error rate
fielding["ErrorRate"] = (
    fielding["E"] /
    fielding["Chances"]
)
primary_pos = (
    fielding.sort_values("InnOuts", ascending=False)
    .drop_duplicates(["playerID", "yearID"])
    [["playerID", "yearID", "POS"]]
)
