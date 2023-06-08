
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import time
import pandas as pd

start_time=time.time()

url='https://concertful.com/area/poland/'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
tags = bs.find_all('a')
tags=tags[3:103]
links = ['https://concertful.com/' + tag['href'] for tag in tags]

df = pd.DataFrame({'Performer':[], 'Venue':[],'Address':[],'Date':[],'Genre':[]})
for link in links:
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    Performer = bs.find('span',{'class':'performers'}).find('a').text
    Venue = bs.find('span',{'class':'venue_name'}).text
    Address = bs.find('span',{'class':'address'}).find('a').text
    Date=bs.find('th',string='Date:').next_sibling.next_sibling.text.strip()
    Date=Date.replace('\t', '')
    Date=Date.replace('\n', '')
    Genre = bs.find('th',string='Genre:').next_sibling.next_sibling.text
    add = {'Performer':Performer, 'Venue':Venue,'Address':Address,'Date':Date,'Genre':Genre}
    df = df.append(add, ignore_index = True)
df.to_csv('df_beautifulsoup.csv') 

end_time=time.time()
duration=end_time-start_time
print("Time duration: ", duration)
