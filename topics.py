#!/usr/bin/env python
#
# to install: sudo pip install objectpath

import json
from objectpath import *
import operator
import csv

with open('survey.json') as json_data:
    db = json.load(json_data)
    
#print(db)
#print("----------------")

tag_map = {}

sections = Tree(db).execute('$.books[@.name is "Mark"].sections.*')
for section in next(sections):
    print(section)
    print("----\n")
    section_tree = Tree(section);
    reference = section_tree.execute('$.reference')
    print("REFERENCE:" + reference)
    tags = section_tree.execute('$.tags')
    for tag in tags:
        print("TAG:" + tag)
        if (tag in tag_map):
            tag_map[tag].append(reference)
        else:
            tag_map[tag] = [reference]
            
     
print("----------------")
print(tag_map)
print("----------------")

counted_tag_map = {key: len(value) for (key, value) in tag_map.items()}
sorted_tag_list = sorted(counted_tag_map.items(), key=operator.itemgetter(1), reverse=True) 
print(sorted_tag_list)

with open("topics.csv", 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(sorted_tag_list)
            
