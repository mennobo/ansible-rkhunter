#!/bin/sh
rkhunter --propupd
rkhunter --cronjob --vl
/usr/share/rkhunter_whitelister.py
