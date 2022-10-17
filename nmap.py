import os

i = 0

while(1):
 os.system('wget http://192.168.137.81/results/' + str(i) + '.txt')
 os.system('mkdir results' + str(i))
 f = list(open(str(i) + '.txt'))

 for y in f:
  targets = y[:-1].split('/')
  target = targets[2]
  os.system('nmap ' + target + ' > results' + str(i) + '/' + target + '.txt')
  
 i = i + 10

 if i == 510:
  break


os.system('python mysql_port.py')
