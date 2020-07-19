from bs4 import BeautifulSoup
from selenium import webdriver


def get_modpack_urls_list(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    pagination_items = soup.find_all('a', class_='pagination-item')
    num_pages = pagination_items[len(pagination_items)-1].text
    
    retVal = []

    for page_num in range(1, 2):  # int(num_pages)):
        new_page_url = DEPENDENTS_URL + '?page=' + str(page_num)
        # get_urls_in_current_page(new_page_url)
        
        driver.get(new_page_url)
        sub_soup = BeautifulSoup(driver.page_source, 'html.parser')

        modpack_listing_rows = sub_soup.find_all('li', class_='project-listing-row')

        for listing_row in range(0, len(modpack_listing_rows)):
            modpack_urls = modpack_listing_rows[listing_row].find_all('a')
            MODPACK_ICON = 0
            MODPACK_NAME = 1
            MODPACK_AUTHOR = 2
            # 3+ = categories
            url = 'https://www.curseforge.com' + modpack_urls[MODPACK_NAME]['href']
            retVal.append(url)
    
    return retVal


def scrape_modpack_pages(urls):
    for url in urls:
        driver.get(url)
        sub_soup = BeautifulSoup(driver.page_source, 'html.parser')
        project_id      = sub_soup.find(text='Project ID'      ).parent.findNext('span').contents[0]
        date_created    = sub_soup.find(text='Created'         ).parent.findNext('span').contents[0]
        date_updated    = sub_soup.find(text='Updated'         ).parent.findNext('span').contents[0]
        downloads       = sub_soup.find(text='Total Downloads' ).parent.findNext('span').contents[0]
        project_license = sub_soup.find(text='License'         ).parent.findNext('span').contents[0]
        # TODO: figure out a good data structure to store these in.
        


if __name__ == "__main__":
    DEPENDENTS_URL = 'https://www.curseforge.com/minecraft/mc-mods/logistics-pipes/relations/dependents'

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    modpack_urls_all = get_modpack_urls_list(DEPENDENTS_URL)
    print(modpack_urls_all)
    
    scrape_modpack_pages(modpack_urls_all)

    driver.quit()
