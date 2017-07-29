# file operations
import json

def read_file_sample(filename):
    file = open(filename,'r')
    filew = open('duplicate.py', 'w')
    for line in file:
        filew.write(line)
    filew.close()
    file.close()

def serialize_json(obj, filename):
    file = open(filename, 'w')
    json.dump(obj, file)
    file.close()

read_file_sample('samthreads.py')
serialize_json([1, 'Venkatesh', 'Cisco'], 'empdata.json')
