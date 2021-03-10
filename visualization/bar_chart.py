import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scores.txt")

df = pd.melt(df, id_vars="Criterion", var_name="Configuration", value_name="Score")

print(df.head())

ax = sns.catplot(data=df, kind='bar', x="Criterion", y="Score", hue="Configuration", legend=False)
plt.ylim(0, 1)
plt.legend(loc="upper right")
plt.show()
