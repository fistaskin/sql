import os

os.system('ls ~/.local/share/sqlmap/output > cp.txt')

f = list(open('cp.txt'))

for x in f:
 os.system('cd ~/.local/share/sqlmap/output/' + x[:-1] + ' && cp log  /home/roman/sqlmap/' + x[:-1] + '.log')
