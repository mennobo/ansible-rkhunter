#!/usr/bin/env python3
log_list = list()
# with open('../../../rkhunter.log', 'r')as f:
with open('/var/log/rkhunter.log', 'r')as f:
    for line in f:
        log_list.append(line)

printline = list()

log_iterator = iter(log_list)

warning_counter = 0

while (line := next(log_iterator, None)) is not None:
    if "Warning:" in line:
        line = line.replace("Warning", "RootkitHunter Warning (see /var/log/rkhunter.log on host)")
        if ":\n" in line:
            printline.append(line.split('\n')[0])
            while True:
                line = next(log_iterator)
                if '          ' in line:
                    line = line.split('          ')[1]
                    line = line.split(':')[0]
                    printline.append(line + "; ")
                else:
                    printline.append('\n')

                    break
        else:
            printline.append(line)
        warning_counter += 1
# print(printline)
# write_file = open('test.txt', 'a+')
write_file = open('/var/log/output_file.txt', 'a+')
write_file.writelines(printline)



