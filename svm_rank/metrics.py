import pandas as pd
import re


def relevant_doc_iterator(line_iter):
    token_aggregator = list()
    number_tokens = 0
    line = next(line_iter, "no more lines")
    while line != "no more lines":
        tokens = line.split(" ")
        number_tokens += len(tokens)
        token_aggregator.append(tokens)
        line = next(line_iter, "no more lines")
    return len(set(token_aggregator)), number_tokens


with open("corpus_stats.txt", "w+") as f, open("msmarco-docs.trec", "r") as g:
    number_unique, number_tokens = relevant_doc_iterator(g)
    f.write(f"unique number of terms: {number_unique}\nnumber of tokens: {number_tokens}")
