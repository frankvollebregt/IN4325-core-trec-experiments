import sys
import pandas as pd


def extract_query_lengths(file_name, output_file, include_header):
    file = pd.read_csv(file_name, sep="\t", header=None)

    lens = file.loc[:, 1].apply(lambda x: len(str(x)))

    res = pd.DataFrame({'qid': file.loc[:, 0], 'qlen': lens})

    res.to_csv(output_file, sep="\t", index=False, header=include_header is "true")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: extract_query_lengths.py inputFile outputFile [includeHeaders]")
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        headers = "true"
        if len(sys.argv) > 3:
            headers = sys.argv[3]
        extract_query_lengths(infile, outfile, headers)