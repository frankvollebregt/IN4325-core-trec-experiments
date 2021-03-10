import pandas as pd

file = pd.read_csv("dev.top100.txt", sep=" ", header=None)
useful = file.iloc[:, [0, 2, 3]]
dat_format = useful.copy()

# set first col as complement of rank
dat_format.iloc[:, 0] = 101 - file.iloc[:, 3]
# Switch cols to dat_format position
dat_format.iloc[:, 1] = file.iloc[:, 0]
dat_format.iloc[:, 2] = file.iloc[:, 2]

dat_format.to_csv(r"dev.without_vec.txt", sep="\t", index=False, header=False)
print(dat_format)
