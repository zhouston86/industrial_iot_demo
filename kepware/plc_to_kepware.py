import sys
import csv


header = 'Tag Name,Address,Data Type,Respect Data Type,Client Access,Scan Rate,Scaling,Raw Low,Raw High,Scaled Low,Scaled High,Scaled Data Type,Clamp Low,Clamp High,Eng Units,Description,Negate Value'

header_attr = header.lower().replace(" ", "_").split(",")


class KepwareObject():
    def __init__(self):
        self.tag_name = None
        self.address = None
        self.datatype = None
        self.type = None
        self.description = None

    def print(self):
        print("address:", self.address)
        print("tag_name:", self.tag_name)
        print("datatype:", self.datatype)
        print("type:", self.type)
        print("description:", self.description)


def check_data_type(tag):
    tag = str(tag)
    if tag[0:2] == 'B3':
        return 'Boolean'
    if tag[0:2] == 'B9':
        return 'Boolean'
    if tag[0:2] == 'F8':
        return 'Float'
    if tag[0:2] == 'N7':
        return 'Word'
    if tag[0:3] == 'N10':
        return 'Word'
    if tag[0:2] == 'T4':
        return 'Word'


kpw_objects = []

# parse plc export to create kepserver tag config. index is column #
# TODO update to use datatables
with open('./plc/PLCIII.csv', newline='') as plc_csv:
    reader = csv.reader(plc_csv, delimiter=','),
    for row in reader:
        for row_list in row:
            index = 0
            new_kpw_object = KepwareObject()
            while index in range(len(row_list)):
                if index == 0:
                    new_kpw_object.address = str(row_list[index])
                    new_kpw_object.datatype = check_data_type(row_list[index])
                if index == 2:
                    new_kpw_object.tag_name = str(row_list[index])
                if index == 3:
                    new_kpw_object.type = str(row_list[index])
                if index == 4:
                    new_kpw_object.description = str(row_list[index])
                index += 1
            kpw_objects.append(new_kpw_object)

kpw_objects[10].print()

f = open('kepware_import.csv', 'w')
f.write(header)
f.write('\n')

# TODO use datatable
for each in kpw_objects:
    if each.datatype is not None:
        write_string = '"{0}", {1}, {2}, 1, r, 100,,,,,,,,,,"{3}",'.format(
            each.address, each.address, each.datatype, each.description)
        f.write(write_string)
        f.write('\n')
