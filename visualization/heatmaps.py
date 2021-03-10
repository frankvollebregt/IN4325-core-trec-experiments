# creates heat maps given the file containing all trec eval results for different parameter settings
# assuming the order is correct

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_heatmaps():
    # b values
    bs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # k1 values
    ks = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]

    with open("trec_evals.txt") as file:
        lines = file.readlines()

        data = []

        l_index = 3
        for b in bs:
            for k in ks:
                line = lines[l_index]
                score = float(line.split(' ')[-1].split('\n')[0])
                data.append([b, k, score])
                l_index += 6

        df = pd.DataFrame(data, columns=['b', 'k_1', 'score'])

        print(df.head())

        df = df.pivot("b", "k_1", "score")
        sns.heatmap(df, vmin=0.3, vmax=0.42)
        plt.show()


if __name__ == '__main__':
    generate_heatmaps()
