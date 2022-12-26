#TODO: only add tags in nam_mapping.csv
#TODO: 


import json
import os
import csv


f = open('ignition_tags/tag_export.json')
io_tags = json.load(f)

csv_dict = {}

with open('ignition_tags/manual_name_mapping.csv') as csv_f:
  csv_reader = csv.DictReader(csv_f)
  for row in csv_reader:
    print(row)
    csv_dict[row['io']] = row['name']

#print(csv_dict.keys())
    

if os.path.exists('ignition_tags/reference_import.json'):
    os.remove('ignition_tags/reference_import.json')

fout = open('ignition_tags/reference_import.json', 'w')

tag_dict_list = []


for i in io_tags['tags'][1]['tags']:
    # ignore ignition system tags that start with "_"
    if i['name'][0] != '_':
      new_dict_entry = {}

      tag_lookup_name = str(i['name']).replace("_","/")
      #print(tag_lookup_name)

      if tag_lookup_name in csv_dict.keys():
          
        new_dict_entry["valueSource"] = "reference"
        new_dict_entry["tagType"] = "AtomicTag"
        new_dict_entry["dataType"] = i['dataType']
        new_dict_entry["name"] = csv_dict[tag_lookup_name]
        new_dict_entry["sourceTagPath"] = "[~]Device1/{0}".format(i['name']) + ".value"

        tag_dict_list.append(new_dict_entry)

json_export = {
  "name":"", 
  "tagType":"Provider", 
  "tags": [
    {
      "name": "DerivedTags",
      "tagType": "Folder",
      "tags": tag_dict_list 
    }]}

#print(json.dumps(json_export,indent=4))

fout.write(json.dumps(json_export,indent=4))