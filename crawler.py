import time 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from collections import Counter 

nodes = []

def CrawlFlowPage(urls):
    driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
    for link in urls: 
        driver.get(link) 
        time.sleep(5)
        elements = driver.find_elements(By.CLASS_NAME ,"nodeTypeList")
        if (len(elements)!=0):
            li_elements = elements[0].find_elements(By.TAG_NAME, "li")
        for li in li_elements:
            try:
                nodes.append(li.text.split(" ")[0].strip(" "))
            except:
                print("error happened")
    counts = Counter(nodes)
    print(counts)
 


urls = [] 
url = 'https://flows.nodered.org/search?type=flow&sort=downloads&page=' 
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 


for i in range(1,10):
    driver.get(url+str(i)) 
    time.sleep(5)
    elements = driver.find_elements(By.XPATH ,"//a[@href]")
    href_values = [element.get_attribute("href") for element in elements]
    for href in href_values:
        if ("flow/" in href):
            print(href)
            urls.append(href)

driver.quit()

CrawlFlowPage(urls)
