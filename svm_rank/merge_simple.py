import pandas as pd
import numpy as np

from functools import lru_cache


DOC_LIMIT = 0


@lru_cache(maxsize=5000)
def get_vec(doc_id):
    return lengths_and_unique.loc[lengths_and_unique["docid"] == doc_id]


# Read files to be merged
dat_format = pd.read_csv("test.top100.txt", sep="\t", header=None)
lengths_and_unique = pd.read_csv("doc_id_lengths_unique", sep="\t", header=None)
lengths_and_unique.columns = ["docid", "doc_len", "unique"]

if DOC_LIMIT:
    dat_format = dat_format.iloc[:DOC_LIMIT, :]
lengths_and_unique = lengths_and_unique.iloc[1:, :]


doc_vecs = pd.DataFrame(np.empty((dat_format.shape[0], 2)), dtype=str)
for i in range(dat_format.shape[0]):
    doc_id = dat_format.iloc[i, 2]
    row = get_vec(doc_id).reset_index()
    if len(row) > 0:
        doc_vecs.at[i, 0] = row.at[0, 'doc_len']
        doc_vecs.at[i, 1] = row.at[0, 'unique']
    else:
        doc_vecs.at[i, 0] = None
        doc_vecs.at[i, 1] = None
        print(f"no match found for document: {dat_format.iloc[i, 2]}")

left_side = dat_format.iloc[:, [0, 1]]
merged = pd.concat([left_side, doc_vecs, dat_format.iloc[:, 2]], axis=1)
merged.columns = ["score", "qid", "doc_len", "unique", "docid"]
merged.to_csv("test.without_bm25.txt", index=False, sep=" ", header=False)
print(merged)


