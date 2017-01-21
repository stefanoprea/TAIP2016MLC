#!/usr/bin/env python3

import csv

data_file = "test.csv"

with open(data_file, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
    for row in reader:
        pair = row[1]
        scores = [int(x) for x in row[2].split(",")]
        score = 0
        count = 0;
        for (index, x) in enumerate(scores):
            score += x * index
            count += x
        if count == 0:
            continue
        score = score / count

        print(pair, "\t", score)
