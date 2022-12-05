import json
import os


f = open('ignition_tags/tag_export.json')
io_tags = json.load(f)

if os.path.exists('ignition_tags/opc_tags.json'):
    os.remove('ignition_tags/opc_tags.json')

if os.path.exists('ignition_tags/reference_import.json'):
    os.remove('ignition_tags/reference_import.json')

fout = open('ignition_tags/reference_import.json', 'w')
opcfout = open('ignition_tags/opc_tags.json', 'w')

fout.write("""
{
  "name": "",
  "tagType": "Provider",
  "tags": [
    {
      "name": "DerivedTags",
      "tagType": "Folder",
      "tags": [
    """)

for i in io_tags['tags'][1]['tags']:
    if i['name'][0] != '_':
        jstr = json.dumps(i , indent=4)
        print(jstr)
        opcfout.write(jstr)
        opcfout.write(',\n')


        fout.write("\t\t{\n")
        fout.write('\t\t"valueSource": "reference",\n')
        fout.write('\t\t"tagType": "AtomicTag",\n')
        fout.write('\t\t"dataType": "{0}",\n'.format(i['dataType']))
        fout.write('\t\t"name": "{0}",\n'.format(i['name']))
        fout.write('\t\t"sourceTagPath": "[~]Device1/{0}"\n'.format(i['name']))
        fout.write("\t\t},\n")




fout.write("]]}")

"""
          "valueSource": "reference",
          "dataType": "Boolean",
          "sourceTagPath": "[~]Device1/B3:0_0.value",
          "name": "FS-1",
          "tagType": "AtomicTag"
"""