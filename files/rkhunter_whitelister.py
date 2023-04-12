#!/usr/bin/env python3
log_list = list()
with open('/var/log/rkhunter.log', 'r')as f:
    for line in f:
        log_list.append(line)

printline = []

log_iterator = iter(log_list)

while (line := next(log_iterator, None)) is not None:
    if "[ Warning ]" in line:
        line = line.split('   ')[1]
        if "/dev" in line or 'hidden' in line:
            continue
        else:
            printline.append(f'SCRIPTWHITELIST={line}\n')

print(printline)
write_file = open('/etc/rkhunter.conf', 'a')
write_file.writelines(printline)
