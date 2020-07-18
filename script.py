from bs4 import BeautifulSoup
from selenium import webdriver
dependents_url = 'https://www.curseforge.com/minecraft/mc-mods/logistics-pipes/relations/dependents'

driver = webdriver.Chrome()
driver.get(dependents_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
modpack_list = soup.find_all('li', class_='project-listing-row box py-3 px-4 flex flex-col lg:flex-row lg:items-center mb-2')

for i in range(0, len(modpack_list)):
    modpack_urls = modpack_list[i].find_all('a')
    # 0 = modpack icon
    # 1 = modpack url
    # 2 = modpack author
    # 3+ = categories
    url = 'https://www.curseforge.com' + modpack_urls[1]['href']
    driver.get(url)

# First iterate throug the pageinated lists to get a complete list of urls for all the modpacks.
# Then, go through those URLs to collect the metadata.

driver.quit()