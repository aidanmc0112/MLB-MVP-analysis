
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
