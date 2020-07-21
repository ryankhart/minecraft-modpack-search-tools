from bs4 import BeautifulSoup
from selenium import webdriver
import re
import json


def get_modpack_paths_list(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pagination_items = soup.find_all('a', class_='pagination-item')
    num_pages = pagination_items[len(pagination_items)-1].text
    
    return_value = []

    for page_num in range(1, int(num_pages)):
        new_page_url = url + '?page=' + str(page_num)
        
        driver.get(new_page_url)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        modpack_listing_rows = soup.find_all('li', class_='project-listing-row')

        for listing_row in range(0, len(modpack_listing_rows)):
            modpack_urls = modpack_listing_rows[listing_row].find_all('a')
            path = modpack_urls[1]['href'] # TODO: do the .parent.findNext() thing on this later for robustness
            return_value.append(path)
    
    return return_value


def write_json(data, filename='data.json'):
    with open(filename, 'w+') as f:
        json.dump(data, f, indent=4)


def initialize_json_file():
    with open('data.json', 'w') as fp:
        data = {}
        data['modpack_metadata'] = []
        json.dump(data, fp)


def get_license_path(project_id):
    return '/project/' + project_id + '/license'


def scrape_modpack_pages(paths):
    ALL_FILES_REL_PATH = '/files/all'
    initialize_json_file()
    for path in paths:
        webdriver_load_from_path(path+ALL_FILES_REL_PATH)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        aside = soup.find('aside')
        header = soup.find('header')
        
        # Header
        project_name = header.find('h2').contents[0]
        
        # Aside
        project_id       = aside.find(text=re.compile('Project ID'     )).parent.find_next('span').contents[0]
        date_created     = aside.find(text=re.compile('Created'        )).parent.find_next('span').find('abbr', class_='standard-datetime')['data-epoch']
        date_updated_tag = aside.find(text=re.compile('Updated'        )).parent.find_next('span').find('abbr', class_='standard-datetime')
        try:
            date_updated = date_updated_tag['data-epoch']
        except:
            continue
        total_downloads  = aside.find(text=re.compile('Total Downloads')).parent.find_next('span').contents[0]
        total_downloads  = int(total_downloads.replace(',', ''))
        # TODO: collect "members" data
        
        # Files (for a list of game versions)
        # TODO: Fix it so that it just passes over modpacks that don't have any files, like "AlliedKingdom In The Sky"
        try:
            table = soup.find_all('table')[0]
        except:
            continue
        header_row = table.find_all('th')
        rows = table.find_all('td')
        version_col = -1
        for col_counter in range(0, len(header_row)):
            header = header_row[col_counter].get_text().strip()
            if 'version' in header.lower():
                version_col = col_counter
        game_versions = set()
        for col_counter in range(1, len(rows)):
            if col_counter == version_col:
                game_versions.add(rows[col_counter].get_text().strip().split('\n')[0].strip())
        
        metadata = {
            'project_name'   : project_name   ,
            'project_id'     : project_id     ,
            'date_created'   : date_created   ,
            'date_updated'   : date_updated   ,
            'total_downloads': total_downloads,
            'game_versions'  : list(game_versions)
        }
        
        with open('data.json', "r+") as json_file: 
            data = json.load(json_file) 
            data['modpack_metadata'].append(metadata)
        
        write_json(data)


def webdriver_load_from_path(path):
    driver.get(CURSEFORGE_DOMAIN + path)


if __name__ == "__main__":
    CURSEFORGE_DOMAIN = 'https://www.curseforge.com'
    DEPENDENTS_URL = 'https://www.curseforge.com/minecraft/mc-mods/logistics-pipes/relations/dependents'

    option = webdriver.ChromeOptions()
    chrome_prefs = {}
    option.experimental_options["prefs"] = chrome_prefs
    
    # Disable images
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    
    # Disable Javascript
    chrome_prefs['profile.managed_default_content_settings.javascript'] = 2

    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)

    #TODO: put get_modpack_paths_list() and scrape_modpack_pages() into 2 separate scripts maybe?
    modpack_paths = get_modpack_paths_list(DEPENDENTS_URL)
    
    scrape_modpack_pages(modpack_paths)
    # scrape_modpack_pages(['/minecraft/modpacks/alliedkingdom-in-the-sky'])

    driver.quit()
