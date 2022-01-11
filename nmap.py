import os

f = list(open('hosts.txt'))

for x in f:
 os.system('nmap ' + x[:-1] + ' > results3/' + x[:-1] + '.txt')

