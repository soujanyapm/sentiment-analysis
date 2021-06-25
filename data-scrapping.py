from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from time  import sleep

import pandas as pd

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#etsy = "https://www.etsy.com/in-en/c/jewelry/earrings/ear-jackets-and-climbers"

browser = webdriver.Chrome(executable_path="../chromedriver",chrome_options=options)

#browser.get(etsy) # website url opens

sleep(0.1)

#each_prod = browser.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div/div/ul/li[1]/div/a")

#each_prod.click()

#all_prods = browser.find_element_by_class_name("responsive-listing-grid")


reviews=[]


for c in range(63,251):
    try:
        print(c)
        browser.get("https://www.etsy.com/in-en/c/jewelry/earrings/ear-jackets-and-climbers?ref=pagination&page={}".format(c))
        print("https://www.etsy.com/in-en/c/jewelry/earrings/ear-jackets-and-climbers?ref=pagination&page={}".format(c))
        
        bs = BeautifulSoup(browser.page_source,'html.parser')
        sleep(0.1)
        all_prods = bs.find("ul",class_="responsive-listing-grid")
       
        links=[]
        
        for row in all_prods.find_all('li'):
            a = row.find("div",class_="js-merch-stash-check-listing").find("a")['href']
            links.append(a)
        
        print(len(links),"LINKS LENGTH")    
            
        for link in links:
            browser.get(link)
            bs = BeautifulSoup(browser.page_source,'html.parser')
            review = bs.find_all('div',class_='wt-content-toggle--truncated-inline-multi')
            print(len(review))
            for eachreview in review:
                #testrev = eachreview.find_element_by_class_name('wt-grid__item-xs-12').find_element_by_class_name('wt-pl-xs-8').find_element_by_class_name('wt-mb-xs-3').
                testrev = eachreview.find('p',class_='wt-text-truncate--multi-line')
             
                reviews.append(testrev.text)
                print(len(reviews),"REVIEWS")
    except:
        browser.close()
        
 
df = pd.DataFrame()    

df['reviews'] = reviews   

df.to_csv('scrapped_reviews_3.csv',index=False)

"""dataframes = []
filenames =["scrapped_reviews.csv","scrapped_reviews_2.csv","scrapped_reviews_3.csv"]
# read all the csv files as dataframes and store them in an array
for f in filenames:
    dataframes.append(pd.read_csv(f))
   
# concatenate all the dataframes row wise and  ignore the index column    
finaldf = pd.concat(dataframes, axis = 0, ignore_index = True)

# Store the concatenated dataframe as csv file. 
finaldf.to_csv("scrapped_reviews_final.csv", index = False)    

test = pd.read_csv("scrapped_reviews_final.csv")

test.shape"""