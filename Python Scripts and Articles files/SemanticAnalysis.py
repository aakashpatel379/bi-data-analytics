import csv
import os
import re
import sys
import math


def wordCounter(word):
    count = 0
    for filename in filelist:
        subpath = path + "\\" + filename
        article_file = open(subpath, "r")
        text = article_file.read()
        # Cleaning
        content = re.sub(r' https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
        content = re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
        if content.count(word) > 0:
            count += 1

        article_file.close()
    return count


directory_name = "Articles_Export"
if not os.path.exists(directory_name):
    print("No directory exists!")
    sys.exit()
path = os.getcwd()
path = path + "\\" + directory_name + "\\"
filelist = os.listdir(path)
N = (len(filelist))
print("N = " + str(N))
words = ['Canada', 'Halifax', 'Nova Scotia']
for w in words:
    count = wordCounter(w)
    print(w + " occured " + str(count) + " times")
    print("Total Documents(N)/ Number of documents appeared (df) :")
    if count != 0:
        tmp = N / count
        print(tmp)
        print("Log10(N/df) :" + str(math.log10(tmp)))

    else:
        print("Infinite");

occuranceList = []
maxRelFreq = 0
articleName = ''
for filename in filelist:
    word = "Canada"
    count = 0
    subpath = path + "\\" + filename
    article_file = open(subpath, "r")
    text = article_file.read()
    total = text.split()
    if text.count(word) > 0:
        count += len(re.findall(word, text))
        relativeFreq = count /len(total)
        res = [filename, str(len(total)), str(count), str(relativeFreq)]
        occuranceList.append(res)
        if maxRelFreq < relativeFreq:
            maxRelFreq = relativeFreq
            articleName =filename
    article_file.close()

semantic = open("semantic_results.csv", "w+", newline='', encoding="utf-8")
semantic = csv.writer(semantic, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
semantic.writerow(['Article', 'Total Words(m)', 'Frequency(f)', 'Relative Freq (f/m)'])
for item in occuranceList:
    semantic.writerow([item[0], item[1], item[2], item[3]])
print("File with semantic results output generated!")
print("\nArticle with maximum relative frequency: ")
print("".join(m for m in articleName))
print("Maximum relative Frequency: " )
print(maxRelFreq)