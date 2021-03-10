# This script runs retrieval for all b and k_1 values and generates files to be processed by run_trec_evals.py

import os


def run_evals():
    # b values
    bs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # k1 values
    ks = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]

    for b in bs:
        for k in ks:
            # run the analysis
            command = "target/appassembler/bin/SearchCollection -topicreader TsvInt" \
                      " -index indexes/msmarco-doc/lucene-index-msmarco" \
                      " -topics src/main/resources/topics-and-qrels/topics.msmarco-doc-2019.txt" \
                      " -output runs/run.msmarco-doc.bm25.b{}.k{}.txt -bm25.b {} -bm25.k1 {} -bm25".format(b, k, b, k)
            print('Running for b = {}, k1 = {}'.format(b, k))
            os.system(command)


if __name__ == '__main__':
    run_evals()
