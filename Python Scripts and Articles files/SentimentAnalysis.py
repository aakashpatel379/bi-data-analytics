import re
import sys
from collections import defaultdict
import csv
from collections import defaultdict
import pandas as pd

# to read positive and negative words

def process_chunk(row):
    dict = {}
    words = row.split()
    for w in words:
        dict[w] = dict.get(w, 0) + 1
    # print(dict)
    positive = 0
    negative = 0
    matches = []
    for key in dict:
        if key in positiveList:
            # increase positive count
            positive += dict[key]
            matches.append(key)

        elif key in negativeList:
            # increase negative count
            negative += dict[key]
            matches.append(key)

    if negative < positive:
        polarity = "positive"
    elif negative == positive:
        polarity = "neutral"
    else:
        polarity = "negative"

    return polarity, matches


positiveWords = open("PositiveWords.txt", "r")
content = positiveWords.read()
positiveList = content.split("\n")
negativeWords = open("NegativeWords.txt", "r")
content = negativeWords.read()
negativeList = content.split("\n")
df = pd.read_csv('clean_search.csv')
sentiment_csv = open("sentiment_results.csv", "w+", newline='', encoding="utf-8")
sentiment_csv = csv.writer(sentiment_csv, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
sentiment_csv.writerow(['Tweet', 'Message', 'Matches', 'Polarity'])
count = 1
for row in df['Tweet']:
    # Cleaning
    content = re.sub(r' https?:\/\/.*[\r\n]*', '', row, flags=re.MULTILINE)
    content = re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
    polarity, matches = process_chunk(content)
    sentiment_csv.writerow([count, content, ','.join(matches), polarity])
    count += 1

print("Sentiments Analysis results CSV file generated!")
