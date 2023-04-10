#!/bin/sh
rkhunter --propupd
rkhunter --cronjob
/usr/share/rkhunter_whitelister.py
