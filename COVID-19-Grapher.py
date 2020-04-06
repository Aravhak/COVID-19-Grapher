import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import operator

countries = {}


URL = 'https://www.worldometers.info/coronavirus/'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(URL, headers=headers)
 
soup = BeautifulSoup(page.content, 'html.parser')


#Web Scraper
Table = soup.findChildren("table")

my_table = Table[0]

rows = my_table.findChildren(['tr'])

for row in rows[2:7]:
    cells = row.findChildren(['td'])
    countries[cells[0].string] = float((cells[1].string).replace(',',''))
    

   
#Bar Graph Set Up 
labels = countries.keys()
cases = countries.values()

y_pos = np.arange(len(labels))


plt.bar(y_pos, cases, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
plt.ylabel('Number of COVID-19 Cases')
plt.title('COVID-19 Cases by Countries')

plt.show()

