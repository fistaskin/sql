f = list(open('hosts.txt'))
res = []

for x in f:
 resi = list(open('results3/' + x[:-1] + '.txt'))
 for y in resi:
  if y[:-1][:4] == '3306':
   res.append(x)
  else:
   continue

r = open('mysql.txt', 'w')

for x in res:
 r.write('http://' + x)

r.close()
