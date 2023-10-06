from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome()
browser.get(url)
time.sleep(10)

planets_data=[]

def scrapping():
    for i in range(0,10):
        time.sleep(2)
        soup=BeautifulSoup(browser.page_source,"html.parser")
        tr_tags=soup.find_all("tr")
        temp_list=[]
        for tr in tr_tags():
            td_tags=tr.find_all("td")
            for i,td in td_tags():
                if i==1:
                    temp_list.append(td.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td.contents[0])
                    except:
                        temp_list.append("")

            hyperlink=td_tags[0]
            temp_list.append('https://exoplanets.nasa.gov'+hyperlink.find_all("a",href=True)[0]['href'])
            planets_data.append(temp_list)



headers=['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date','hyperlink']
planet_df=pd.DataFrame(planets_data,columns=headers)
planet_df.to_csv("scrapped_data.csv",index=True,index_label='id')