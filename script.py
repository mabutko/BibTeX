import bibtexparser
import csv
from operator import itemgetter

with open('sciencedirect.bib', encoding="utf8") as sciencedirect_file:
    sciencedirect_results = bibtexparser.load(sciencedirect_file)

with open('ieee.bib', encoding="utf8") as ieee_file:
    ieee_results = bibtexparser.load(ieee_file)

with open('scopus.bib', encoding="utf8") as scopus_file:
    scopus_results = bibtexparser.load(scopus_file)

with open('acm.bib') as acm_file:
    acm_results = bibtexparser.load(acm_file)

results = [[0] * 4 for i in range(len(sciencedirect_results.entries)+len(ieee_results.entries)+len(scopus_results.entries)+len(acm_results.entries))]
i = 0
remove_content = ["https://doi.org/"] # Content you want to be removed from `str`

for x in range(len(sciencedirect_results.entries)):
    for content in remove_content:
        sciencedirect_results.entries[x]['doi'] = sciencedirect_results.entries[x]['doi'].replace(content, '')
    results[i][0] = (sciencedirect_results.entries[x]['title'])
    results[i][1] = (sciencedirect_results.entries[x]['author'])
    results[i][2] = (sciencedirect_results.entries[x]['year'])
    results[i][3] = (sciencedirect_results.entries[x]['doi'])
    i = i + 1

remove_content = ["{", "}"] # Content you want to be removed from `str`

for x in range(len(ieee_results.entries)):
    for content in remove_content:
        ieee_results.entries[x]['author'] = ieee_results.entries[x]['author'].replace(content, '')
    results[i][0] = (ieee_results.entries[x]['title'])
    results[i][1] = (ieee_results.entries[x]['author'])
    results[i][2] = (ieee_results.entries[x]['year'])
    results[i][3] = (ieee_results.entries[x]['doi'])
    i = i + 1

for x in range(len(scopus_results.entries)):
    results[i][0] = (scopus_results.entries[x]['title'])
    results[i][1] = (scopus_results.entries[x]['author'])
    results[i][2] = (scopus_results.entries[x]['year'])
    results[i][3] = (scopus_results.entries[x]['doi'])
    i = i + 1

for x in range(len(acm_results.entries)):
    results[i][0] = (acm_results.entries[x]['title'])
    results[i][1] = (acm_results.entries[x]['author'])
    results[i][2] = (acm_results.entries[x]['year'])
    results[i][3] = (acm_results.entries[x]['doi'])
    i = i + 1

double_list = []

for x in range(len(results)):
    test = results[x][3]
    for z in range(len(results)):
        if x != z:
            if test == results[z][3]:
                double_list.append(test)
double_list = list(set(double_list))

results = sorted(results, key=itemgetter(0))

total_no = len(results)
for t in range(len(double_list)):
    flag = 0
    x = 0
    while x < total_no:
        if flag == 0:
            if results[x][3] == double_list[t]:
                flag = 1
                results.pop(x)
                total_no = total_no -1
                x = x+1
            else:
                x = x+1
        else:
            x = x+1

with open('file.csv', 'w', newline='') as csvfile:
    csvfile.write('"' + 'TITLE' + '"' + ',' + '"' + 'AUTHOR' + '"' + ',' + '"' + 'YEAR' + '"' + ',' + '"' + 'DOI' + '"' + ',')
    csvfile.write('\n')
    for row in results:
        for x in row:
            csvfile.write('"' + str(x) + '"' + ',')
        csvfile.write('\n')