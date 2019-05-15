#!/bin/bash
. ./openrc.sh
sudo ansible-playbook  --inventory ./inventory/hosts.ini  --ask-become-pass -u ubuntu wholeSystem.yaml
