#!/usr/bin/python
# check_docker.py
# This program performs a 'docker ps' command, looks for specific information
#   needed to verify the ContextSDM processes are running.

import sys
from subprocess import Popen, PIPE, STDOUT, call

if len(sys.argv) != 2:
    exit('One container not specified')
else:
    container = sys.argv[1]

proc=Popen('docker ps', shell=True, stdout=PIPE,)
output=proc.communicate()[0]
lines = output.split('\n')

# 1) Get output of 'docker ps' command, which is returned as a string.  For testing use docker.txt

# 2) Break output into lines
# text_file = open('docker.txt', 'r')
# lines = text_file.readlines()

# 3) For first line get starting location of each field.  field_list is a list of dictionary as
#    [ column_name: start]
heading = lines[0]
fields = {'CONTAINER ID':0, 'IMAGE':0, 'COMMAND':0, 'CREATED':0, 'STATUS':0, 'PORTS':0, 'NAMES':0}

for key in fields.keys():
    fields[key] = heading.find(key)

for line in lines[1:]:
    status = line[fields['STATUS']:fields['PORTS']-1]
    name = line[fields['NAMES']:].strip()

    if (name.find(container) != -1):
        if (status.find('Up') != -1):
            print(f'{name}: {status}')
            exit(0)
        else:
            exit(f'{name}: {status}')

exit(f'{container} not found')

