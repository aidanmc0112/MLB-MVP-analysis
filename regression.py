def run_regression(full_data):
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
    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )
    
    
    model.fit(
        X_train,
        y_train
    )
    test["PredictedVoteShare"] = model.predict(X_test)
    predictions = test.sort_values(
        "PredictedVoteShare",
        ascending=False
    )
    for league in ["AL","NL"]:
        print("\n", league)
    
        print(
            predictions[
                predictions["lgID"] == league
            ][
                [
                    "nameFirst",
                    "nameLast",
                    "PredictedVoteShare",
                    "VoteShare"
                ]
            ].head(10)
        )
    return model
