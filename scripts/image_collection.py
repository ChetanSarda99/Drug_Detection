#Script for collecting images

# from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
#driver =webdriver.Chrome(options=options)
#for _ in range(65, 66):
#    url = f'https://www.drugs.com/alpha/{_}.html'
#    driver.get(url)
#    driver.find_element_by_xpath('/html/body/main/div/div[1]/div[2]/ul')

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

image_save =  r'C:\Users\sarda\OneDrive\Desktop\PythonCodes\PotfolioProjects\ImageRecogWebScrape\data\raw\images'
drug_imprints=[]
drug_details=[]
drug_imprints=[]
drug_names=[]
drug_counts=[]
for _ in range(65, 95):
    _=chr(_).lower()
    url = f'https://www.drugs.com/alpha/{_}.html'
    soup = BeautifulSoup(urlopen(url),features="html.parser")
    list = soup.find('ul', attrs={'class': 'ddc-list-column-2'})
    href_tags = list.find_all('a',href=True)
    for a in href_tags:
        c=0
        drug_url= f"https://www.drugs.com{a['href']}"
        drug_soup = BeautifulSoup(urlopen(drug_url),features="html.parser")
        try:
            drug_larger_url = 'https://www.drugs.com'+ drug_soup.find('div', attrs={'class': 'drugImageHolder'}).findAll('a',href=True)[0]['href']
            imprint_soup = BeautifulSoup(urlopen(drug_larger_url),features="html.parser")
            imprint_soup_images_div = imprint_soup.find('div', attrs={'class': 'ddc-grid-col-6 ddc-pid-info-images'})
            images = imprint_soup_images_div.findAll('img',src=True)
            imprint_text_soup = imprint_soup.find('div', attrs={'class': 'ddc-grid-col-6 pid-info'})
            #print(imprint_text_soup)
            drug_name= imprint_text_soup.find('h3').text
            drug_imprint = imprint_soup.find('h2').text
            drug_detailed= imprint_soup.find('h1').text
            if drug_imprint == 'Images of medication':
                pass
            else:
                drug_imprint=drug_imprint.replace('Images for ','')
                for image in images:
                    img_data = requests.get(image['src']).content
                    c=c+1
                    with open(f'{image_save}\\{drug_name}--{drug_imprint}--{c}.jpg ', 'wb') as handler:
                        handler.write(img_data)
                        print(f'{drug_name}--{drug_imprint}--{c}')
                    drug_imprints.append(drug_imprint)
                    drug_details.append(drug_detailed)
                    drug_names.append(drug_name)
                    drug_counts.append(c)
        except:
            pass
    drugs = pd.DataFrame()
    drugs['drug_name']=drug_names
    drugs['drug_imprint']=drug_imprints
    drugs['drug_detailed']=drug_details
    drugs['drug_count']=drug_counts
    drugs.to_csv(r'C:\Users\sarda\OneDrive\Desktop\PythonCodes\PotfolioProjects\ImageRecogWebScrape\data\raw\drugs.csv',index=False)
