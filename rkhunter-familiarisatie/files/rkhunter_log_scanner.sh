#!/bin/sh
/usr/bin/rkhunter --cronjob
/usr/share/rkhunter_log_scanner.py
logger -f /var/log/output_file.txt
