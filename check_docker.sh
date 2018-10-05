#!/bin/bash
# Note: This process depends upon a crontab run as root
#       7,14,21,28,35,42,49,56     *    *     *     *         docker ps > /home/nagiosrm/docker_status.txt

python /home/nagiosrm/plugins/check_docker.py $1
