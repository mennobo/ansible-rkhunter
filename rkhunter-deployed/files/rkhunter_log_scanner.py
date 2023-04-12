#!/usr/bin/env python3
log_list = list()
with open('../../rkhunter.log', 'r')as f:
# with open('/var/log/rkhunter.log', 'r')as f:
    for line in f:
        log_list.append(line)

printline = str()

log_iterator = iter(log_list)

warning_counter = 0

while (line := next(log_iterator, None)) is not None:
    if "Warning:" in line:
        line = line.replace("Warning", "RootkitHunter Warning")
        if ":\n" in line:
            printline += line.split('\n')[0]
            while True:
                line = next(log_iterator)
                if '          ' in line:
                    line = line.split('          ')[1]
                    line = line.split(':')[0]
                    printline += line + "; "
                else:
                    printline += '\n'

                    break
        else:
            printline += line
        warning_counter += 1

# printline = "RKhunter Warnings: " + printline
print(printline)
write_file = open('/var/log/output_file.txt', 'w+')
write_file.write(printline)

