import pandas as pd

run = "group14run2"

test_input = pd.read_csv("svm_test.txt", sep=" ")
# identifiers = test_input.loc[:, ["qid", "docid"]]
score = pd.read_csv("predictions_c1_e0001", header=None)
n_rows = score.shape[0]
rank = pd.Series(1).repeat(n_rows)

trec_data = pd.concat([
    test_input.loc[:, "qid"].reset_index(drop=True),
    pd.Series("Q0").repeat(n_rows).reset_index(drop=True),
    test_input.loc[:, "docid"].reset_index(drop=True),
    rank.reset_index(drop=True),
    score.reset_index(drop=True),
    pd.Series(run).repeat(n_rows).reset_index(drop=True)
], axis=1)

trec_data.columns = ["qid", "Q0", "docid", "rank", "score", "runid"]
trec_format = trec_data.sort_values(by=["qid", "score"], ascending=False)

trec_format.to_csv(f"runs/{run}", index=False, header=False, sep=" ")
