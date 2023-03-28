# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import csv

# START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
# browser = webdriver.Chrome('C:/Users/NXG/Downloads/p-127/chromedriver')
# browser.get(START_URL)
# time.sleep(10)

# def scrape():
#     headers=['Name','Distance','Mass','Radius']
#     planet_data = []
#     for i in range(0,428):
#         soup = BeautifulSoup(browser.page_source,'html.parser')
#         for ul_tag in soup.find_all('ul',attrs = {'class','exoplanet'}):
#             li_tags = ul_tag.find_all('li')
#             temp_list=[]
#             for index,li_tg in enumerate(li_tags):
#                 if index == 0:
#                     temp_list.append(li_tg.find_all('a')[0].contents[0])
#                 else:
#                     try:
#                         temp_list.append(li_tg.contents[0])
#                     except:
#                         temp_list.append('')
#             planet_data.append(temp_list)
#         browser.find_element('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
#     with open('scaper.csv','w')as f:
#         csvw = csv.writer(f)
#         csvw.writerow(headers)
#         csvw.writerow(planet_data)

# scrape()

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('bright_stars.csv')
