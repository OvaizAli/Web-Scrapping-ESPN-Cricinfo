from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


site = 'http://static.cricinfo.com/rss/livescores.xml'
#Open that site
op = urlopen(site) 

# read data from site
rd = op.read() 
# # close the object
op.close()   
# scrapping data from site
sp_page = soup(rd,'xml') 

match_list = sp_page.find_all('description') 
# print(match_list)
for match in match_list:  
    print(match.get_text())
    print('-'*110)
