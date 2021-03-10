import pandas as pd
# import dask.dataframe as pd

# Reading and creating indices
no_bm25 = pd.read_csv("test.without_bm25.txt", sep=" ")
no_bm25.columns = ["score", "qid", "doc_len", "unique", "docid"]
no_bm25.set_index(["qid", "docid"], inplace=True)
bm25 = pd.read_csv("test.bm25.txt", sep="\t")
bm25.set_index(["qid", "docid"], inplace=True)
bm25.columns = ["bm25"]

joined = bm25.join(no_bm25, how="inner")        # Magic super efficient operation

# Adhering to SVM dat format
joined["qid"] = joined.index.get_level_values("qid")
joined["docid"] = joined.index.get_level_values(1)
correct_order = joined[["score", "qid", "bm25", "doc_len", "unique", "docid"]]       # Changing order of columns
correct_order.to_csv("svm_test.txt", index=False, sep=" ")                          # write clean values
correct_order = correct_order.drop(columns="docid")

# Mapping values to SVM compatible format
correct_order.loc[:, "qid"] = correct_order["qid"].map(lambda e: f"qid:{e}")
for index, label in enumerate(["bm25", "doc_len", "unique"]):
    correct_order.loc[:, label] = correct_order[label].map(lambda e: f"{index+1}:{e}")

# print(correct_order.head())
correct_order.to_csv("svm_test.dat", index=False, header=False, sep=" ")   # SVM compatible values
