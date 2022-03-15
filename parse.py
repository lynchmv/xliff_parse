#!/usr/bin/python3

import csv
import lxml.html as lh
import sys

text_file = open(sys.argv[1], "r")
file_parts = sys.argv[1].split('.')
file_root = file_parts[0]
csv_file = file_root + '.csv'

data = text_file.read()
text_file.close()

diff = data
doc = lh.fromstring(diff.encode('utf-8'))
sources = []
targets = []
source = doc.xpath('//source')
target = doc.xpath('//target')
for s in source:
    sources.append(s.text_content())
for t in target:
    targets.append(t.text_content())
fields = ['source', 'target']
allItems = []
with open(csv_file, 'w') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames = fields)
  writer.writeheader()
  for source, target in zip(sources, targets):
    thisItem = {}
    thisItem['source'] = source
    thisItem['target'] = target
    allItems.append(thisItem)
  writer.writerows(allItems)
