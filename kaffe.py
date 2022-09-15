import requests
from bs4 import BeautifulSoup
import xlwings as xw
import xlrd
import time
from datetime import datetime
import re

path = ('C:/Users/willi/Desktop/informatik pack/edeka projekt/edeka.xls')
# für xlrd to read the info...
workbook = xlrd.open_workbook(path)

print('basic info')
print('-------------------------------------------------')
sheet1 = workbook.sheet_by_name('kaffee')
print('name:...'+sheet1.name)
rows = sheet1.nrows  # Zeile
print('---------------------------------------------')
print('Es gibt insgesamt ')
time.sleep(0.5)
print(rows)
print('Zeile')
cols = sheet1.ncols  # Spalten
print(cols)
print('Spalten')
print('---------------------------------------------')
time.sleep(2)

#für xlwings
xlwingswb = xw.Book(path)
xlsheet = xlwingswb.sheets['kaffee']

#für Zeit, ddatetime
now1 = datetime.now()

cookies = {
    'language': '0',
    'sid': 'v05oddiekf0e8930nncer249hm',
    'sid_key': 'oxid',
    'emos_jcsid': 'AYM4Ykp1EUQeQ0R*lamLWUts*wbufoTt:t:1:0',
    '_fbp': 'fb.1.1663098309317.1022366017',
    '_gcl_au': '1.1.607335976.1663098313',
    '_ga': 'GA1.1.850617846.1663098313',
    '_ga_H0G3QQZZ6X': 'GS1.1.1663098312.1.1.1663098410.60.0.0',
}

headers = {
    'authority': 'www.edeka24.de',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    #Requests sorts cookies= alphabetically
    'cookie': 'language=0; sid=v05oddiekf0e8930nncer249hm; sid_key=oxid; emos_jcsid=AYM4Ykp1EUQeQ0R*lamLWUts*wbufoTt:t:1:0; _fbp=fb.1.1663098309317.1022366017; _gcl_au=1.1.607335976.1663098313; _ga=GA1.1.850617846.1663098313; _ga_H0G3QQZZ6X=GS1.1.1663098312.1.1.1663098410.60.0.0',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.get('https://www.edeka24.de/Lebensmittel/Kaffee-und-Tee/Kaffee-ganze-Bohnen/', cookies=cookies, headers=headers)
print (response.status_code)
demo = response.text
time.sleep(2.3)
soup = BeautifulSoup(demo, 'html.parser')
list = {}
amount = soup.find(name ='div',attrs={'class':'category-amount-articles'}).find(name ='span').get_text()
amount = int(amount)
print(amount)

i=0
while i <=amount:
    i=i+1
    num1= str(i)
    link= soup.find_all(name='a',attrs={'href':re.compile(r'^http')}).getlink()
    for links in link.getlink():
        list=links
print(list)
















