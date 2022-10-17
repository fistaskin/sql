i = 0

while(1):
 f = list(open(str(i) + '.txt'))
 res = []

 for x in f:
  targets = x.split('/')
  target = targets[2]
  try:
   resi = list(open('results' + str(i) + '/' + target + '.txt'))
   for y in resi:
    if y[:-2][:4] == '3306':
     res.append(target)
    else:
     continue
  except:
   continue
 r = open('results' + str(i) + '/mysql.txt', 'w')

 for x in res:
  r.write('http://')
  r.write(x)
  r.write('\n')

 r.close()
 i = i + 10
 if i == 510:
  break
