# Takes data from a run, and shows the BM25 score over the rank for the queries on line 9

import pandas as pd
import matplotlib.pyplot as plt


def plot_data(file_name, file_name2):
    # queries
    queries = [1119729, 60235]
    colors = ['red', 'orange', 'blue', 'purple']
    labels = ['Baseline long query', 'Improved long query', 'Baseline short query', 'Improved short query']

    df = pd.read_csv(file_name, sep=" ", header=None, names=['qid', 'Q0', 'docid', 'rank', 'score', 'runid'])
    df2 = pd.read_csv(file_name2, sep=" ", header=None, names=['qid', 'Q0', 'docid', 'rank', 'score', 'runid'])

    ax = None

    # loop over all queries
    for qid in range(len(queries)):
        # get the entire ranking for this query
        onlyquery = df.loc[df['qid'] == queries[qid]]
        onlyquery2 = df2.loc[df2['qid'] == queries[qid]]

        res = onlyquery[["rank", "score"]]
        res2 = onlyquery2[["rank", "score"]]

        if ax is None:
            ax = res.plot(kind="line", x="rank", y="score", color=colors[2*qid], ylabel="BM25 score", label=labels[2*qid])
        else:
            res.plot(kind="line", x="rank", y="score", color=colors[2*qid], ax=ax, label=labels[2*qid])

        res2.plot(kind="line", x="rank", y="score", color=colors[2*qid+1], ax=ax, label=labels[2*qid+1])

    plt.show()


if __name__ == '__main__':
    plot_data('stopwords.without.txt', 'improved-maybe.txt')
