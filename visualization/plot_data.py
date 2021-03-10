import pandas as pd
import matplotlib.pyplot as plt


def plot_data(file_name):
    # queries
    queries = [600573, 1119729, 117831, 60235]
    colors = ['red', 'orange', 'purple', 'blue']
    labels = ['Long query 1', 'Long query 2', 'Short query 1', 'Short query 2']

    df = pd.read_csv(file_name, sep=" ", header=None, names=['qid', 'Q0', 'docid', 'rank', 'score', 'runid'])

    ax = None

    # loop over all queries
    for qid in range(len(queries)):
        # get the entire ranking for this query
        onlyquery = df.loc[df['qid'] == queries[qid]]

        res = onlyquery[["rank", "score"]]

        if ax is None:
            ax = res.plot(kind="line", x="rank", y="score", color=colors[qid], ylabel="BM25 score", label=labels[qid])
        else:
            res.plot(kind="line", x="rank", y="score", color=colors[qid], ax=ax, label=labels[qid])

        print(res)

    plt.show()


if __name__ == '__main__':
    plot_data('run.txt')
