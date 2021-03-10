import pandas as pd
import re


top100 = pd.read_csv("msmarco-doctest2019-top100", header=None, sep=" ")
unique_doc_ids = top100.iloc[:, 2].drop_duplicates()


def relevant_doc_iterator(line_iter):
    line_aggregator = ""
    doc_delimiter_regex = re.compile(r"<DOCNO>(D[0-9]+)</DOCNO>")
    line = next(line_iter, "no more lines")
    while line != "no more lines":
        found = doc_delimiter_regex.search(line)
        if found:
            # Get id of next-in-line document
            doc_id = found.group(1)
            # print(f"now starting document {doc_id}")
            # Decide whether this doc should be saved before reset of doc_aggregator
            if unique_doc_ids.str.contains(doc_id).any():
                print("yielding")
                yield line_aggregator
            line_aggregator = ""
        # Append line to document and get next line
        line_aggregator += line
        line = next(line_iter, "no more lines")


with open("downsized.trec", "w+") as f, open("msmarco-docs.trec", "r") as g:
    doc_iter = relevant_doc_iterator(g)
    f.writelines(doc_iter)



