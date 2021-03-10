import pandas as pd
import matplotlib.pyplot as plt


def plot_data(file_name, file_name2):
    # queries
    # queries = [1119729, 60235]
    # colors = ['red', 'orange', 'blue', 'purple']
    # labels = ['Baseline long query', 'Improved long query', 'Baseline short query', 'Improved short query']

    df = pd.read_csv(file_name, sep="\t", header=None, names=['qid', 'Test queries'])
    df2 = pd.read_csv(file_name, sep="\t", header=None, names=['qid', 'Dev queries'])
    sr = df['Test queries']
    sr2 = df2['Dev queries']

    lens = sr.apply(lambda q: len(str(q).split(' ')))
    lens2 = sr2.apply(lambda q: len(str(q).split(' ')))

    # lens.plot.box(xticks=[])
    final = pd.concat([lens, lens2], axis=1).reset_index()

    print(final.head())

    final.boxplot(column=['Dev queries', 'Test queries'])

    plt.ylabel('Query length in words')
    plt.show()


if __name__ == '__main__':
    plot_data("topics.msmarco-doc-2019.txt", "queries.docdev.tsv")
