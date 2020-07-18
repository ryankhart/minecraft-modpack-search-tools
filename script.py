from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == "__main__":
    dependents_url = 'https://www.curseforge.com/minecraft/mc-mods/logistics-pipes/relations/dependents'

    driver = webdriver.Chrome()

    driver.get(dependents_url)
    driver.implicitly_wait(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    pagination_items = soup.find_all('a', class_='pagination-item')
    num_pages = pagination_items[len(pagination_items)-1].text

    modpack_urls_all = []

    for page_num in range(1, int(num_pages)):
        driver.get(dependents_url + '?page=' + str(page_num))
        driver.implicitly_wait(10)
        sub_soup = BeautifulSoup(driver.page_source, 'html.parser')

        modpack_listing_rows = sub_soup.find_all('li', class_='project-listing-row box py-3 px-4 flex flex-col lg:flex-row lg:items-center mb-2')

        for listing_row in range(0, len(modpack_listing_rows)):
            modpack_urls = modpack_listing_rows[listing_row].find_all('a')
            MODPACK_ICON = 0
            MODPACK_NAME = 1
            MODPACK_AUTHOR = 2
            # 3+ = categories
            url = 'https://www.curseforge.com' + modpack_urls[MODPACK_NAME]['href']
            modpack_urls_all.append(url)
            # driver.get(url)

    print(modpack_urls_all)

    driver.quit()