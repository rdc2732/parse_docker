#!/usr/bin/python
# check_docker.py
# This program performs a 'docker ps' command, looks for specific information
#   needed to verify the ContextSDM processes are running.

import sys
import os
from datetime import datetime

status_file_name = "/home/nagiosrm/docker_status.txt"

if len(sys.argv) != 2:
    exit('One container not specified')
else:
    container = sys.argv[1]

try:
    status_file = open(status_file_name)
except IOError:
    exit (status_file_name + " does not exist.")

status_time = os.path.getmtime("docker_status.txt")
status_time_str = str(datetime.fromtimestamp(status_time))
status_time_message = "Docker Process Status: " + status_time_str

if container == "STATUS":
    print status_time_message
    exit(0)

lines = status_file.readlines()

# For first line get starting location of each field.  field_list is a list of dictionary as
#    [ column_name: start]
heading = lines[0]
fields = {'CONTAINER ID':0, 'IMAGE':0, 'COMMAND':0, 'CREATED':0, 'STATUS':0, 'PORTS':0, 'NAMES':0}

for key in fields.keys():
    fields[key] = heading.find(key)

for line in lines[1:]:
    status = line[fields['STATUS']:fields['PORTS']-1]
    name = line[fields['NAMES']:].strip()
    response = name + ": " + status
    if (name.find(container) != -1):
        if (status.find('Up') != -1):
            print(response)
            exit(0)
        else:
            exit(response)

exit(container + ' not found')

# context-server-pcc_qa
# context-nginx
# clearcase
# teamcenter
# context-redis
# context-server-pc_qa_prod
# context-myadmin
# context-mysql

# To Do:
#   - Create and document de08u2008 cron jobs to create docker ps, docker check time and system ps files
#   - Update python program to read all of these files and return based on query type
#   - Package up the stuff that goes on head CSDM server.  cron scripts, plugins