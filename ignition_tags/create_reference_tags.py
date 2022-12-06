import json
import os


f = open('ignition_tags/tag_export.json')
io_tags = json.load(f)

if os.path.exists('ignition_tags/reference_import.json'):
    os.remove('ignition_tags/reference_import.json')

fout = open('ignition_tags/reference_import.json', 'w')

tag_dict_list = []


for i in io_tags['tags'][1]['tags']:
    if i['name'][0] != '_':
        new_dict_entry = {}


        new_dict_entry["valueSource"] = "reference"
        new_dict_entry["tagType"] = "AtomicTag"
        new_dict_entry["dataType"] = i['dataType']
        new_dict_entry["name"] = i['name']
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

print(json.dumps(json_export,indent=4))

fout.write(json.dumps(json_export,indent=4))