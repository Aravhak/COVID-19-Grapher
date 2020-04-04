import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

countries = {}

URL = 'https://www.worldometers.info/coronavirus/'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(URL, headers=headers)
 
soup = BeautifulSoup(page.content, 'html.parser')

#country1Count = soup.find_all(style="font-weight: bold; text-align:right").get_text()

#print (country1Count)

Table = soup.findChildren("table")

my_table = Table[0]

rows = my_table.findChildren(['tr'])

#print(rows)

for row in rows[2:7]:
    cells = row.findChildren(['td'])
    countries[cells[0].string] = cells[1].string

#print(countries)
    
    
labels = countries.keys()
cases = countries.values()

#print(labels)

y_pos = np.arange(len(labels))

plt.bar(y_pos, cases, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
plt.ylabel('Number of COVID-19 Cases')
plt.title('COVID-19 Cases by Countries')

plt.show()


#total = soup.find('class="sorting_1"').get_text()

#print(total)

#country2Count = soup.find_all_next(style="font-weight: bold; text-align:right").get_text()

#lineHTML = soup.a
#countryTestCount = lineHTML.find_all_next(string=True)

#print (countryTestCount)

#print (country2Count)