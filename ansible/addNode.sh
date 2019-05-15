#!/bin/bash
. ./openrc.sh
sudo ansible-playbook  --inventory ./inventory/harvester2.ini  --ask-become-pass -u ubuntu harvestor2.yaml
