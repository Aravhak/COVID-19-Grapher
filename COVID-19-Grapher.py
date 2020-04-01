import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

countries = ['us', 'italy', 'spain', 'china']

URL = 'https://www.worldometers.info/coronavirus/'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(URL, headers=headers)
 
soup = BeautifulSoup(page.content, 'html.parser')

lineHTML = 'style="font-weight: bold; text-align:right"'

country1Count = soup.find(style="font-weight: bold; text-align:right").get_text()

print (country1Count)

#country2Count = soup.find_all_next(style="font-weight: bold; text-align:right").get_text()

#lineHTML = soup.a
#countryTestCount = lineHTML.find_all_next(string=True)

#print (countryTestCount)

#print (country2Count)