# this script takes the retrieval results and extracts only the qid, docid and score, such that
# the resulting file can be processed for SVM-rank training data

import sys
import pandas as pd


def extract_scores(file_name, output_file, include_header):
    file = pd.read_csv(file_name, sep=" ", header=None)

    res = pd.DataFrame({'qid': file.loc[:, 0], 'docid': file.loc[:, 2], 'score': file.loc[:, 4]})

    res.to_csv(output_file, sep="\t", index=False, header=include_header is "true")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: extract_scores.py inputFile outputFile [includeHeaders]")
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        headers = "true"
        if len(sys.argv) > 3:
            headers = sys.argv[3]
        extract_scores(infile, outfile, headers)
