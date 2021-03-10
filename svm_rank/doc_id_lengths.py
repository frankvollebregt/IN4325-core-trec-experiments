import pandas as pd

file = pd.read_csv("doclens.txt", sep="\t", header=None)

output = file.iloc[:, [1, 2, 3]]

output.to_csv("doc_id_lengths_unique", sep="\t", index=False)

print(file)
