import time 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By


def CrawlFlowPage(url):
    driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
    driver.get(url) 
    time.sleep(3)
    elements = driver.find_elements(By.CLASS_NAME ,"nodeTypeList")
    li_elements = elements[0].find_elements(By.TAG_NAME, "li")
    for li in li_elements:
        print(li.text)



urls = [] 
url = 'https://flows.nodered.org/search?type=flow&page=1' 
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 

driver.get(url) 
time.sleep(3)
elements = driver.find_elements(By.XPATH ,"//a[@href]")
href_values = [element.get_attribute("href") for element in elements]
driver.quit()
for href in href_values:
    if ("flow/" in href):
        print(href)
        urls.append(href)

CrawlFlowPage(urls[0])
