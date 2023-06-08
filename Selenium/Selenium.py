from genericpath import exists
from pickle import TRUE
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

start_time=time.time()

path = "/mnt/c/Users/nomin/chromedriver_linux64/chromedriver"
ser = Service(path)
driver = webdriver.Chrome( service=ser) 
### Following page is the starting page to scrap
url='https://concertful.com/area/poland/'
driver.get(url)
href_links = []

elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
for elem in elems[3:103]:
    l = elem.get_attribute("href")
    if l not in href_links:
        href_links.append(l)

Performer_list=[]
Venue_list=[]
Address_list=[]
Date_list=[]
Genre_list=[]
#elems
for i in href_links:
    driver.get(i)
    Performer=driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/div[1]/div/table/tbody/tr[1]/td/span/a/abbr')
    Performer=Performer.text
    Performer_list.append(Performer)
    Venue=driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/div[1]/div/table/tbody/tr[2]/td/span[1]')
    Venue=Venue.text
    Venue_list.append(Venue)
    Address=driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/div[1]/div/table/tbody/tr[2]/td/span[2]/abbr[1]/a')
    Address=Address.text
    Address_list.append(Address)
    Date=driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/div[1]/div/table/tbody/tr[3]/td')
    Date=Date.text
    Date_list.append(Date)
    Genre=driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/div[1]/div/table/tbody/tr[4]/td')
    Genre=Genre.text
    Genre_list.append(Genre)


#driver.quit()
dictionary = {'Performer': Performer_list,'Venue':Venue_list,
              'Address': Address_list,'Date':Date_list,
              'Genre': Genre_list} 
df = pd.DataFrame(dictionary)
df.to_csv('df_selenium.csv') 

end_time=time.time()
duration=end_time-start_time
print("Time duration: ", duration)
