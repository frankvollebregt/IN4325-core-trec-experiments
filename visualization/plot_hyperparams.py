import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_hyperparams(file_name):
    #score to visualize
    score = "P_50"

    # b values
    bs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # k1 values
    ks = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]

    df = pd.read_csv(file_name, sep=" ", header=None, names=['qid', 'Q0', 'docid', 'rank', 'score', 'runid'])

    ax = None

    # # loop over all queries
    # for qid in range(len(queries)):
    #     # get the entire ranking for this query
    #     onlyquery = df.loc[df['qid'] == queries[qid]]
    #
    #     res = onlyquery[["rank", "score"]]
    #
    #     if ax is None:
    #         ax = res.plot(kind="line", x="rank", y="score", color=colors[qid], ylabel="BM25 score", label=labels[qid])
    #     else:
    #         res.plot(kind="line", x="rank", y="score", color=colors[qid], ax=ax, label=labels[qid])
    #
    #     print(res)
    #
    # plt.show()


if __name__ == '__main__':
    plot_hyperparams('run.txt')
