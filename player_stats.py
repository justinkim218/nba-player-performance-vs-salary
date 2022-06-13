from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PlayerStats:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.soup = self.get_html()
        self.dataframe = self.get_data(self.soup)

    def get_html(self):
        url = "https://www.nba.com/stats/players/advanced/?sort=PIE&dir=-1&Season=2021-22&SeasonType=Regular%20Season&CF=POSS*G*500:GP*G*15:PLAYER_NAME*E*"
        self.driver.get(url)

        show_all_pages = Select(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select'))
        show_all_pages.select_by_index(0)

        source = self.driver.page_source

        self.driver.quit()

        return BeautifulSoup(source, 'html.parser')

    def get_data(self, soup):
        table = soup.find("div", attrs={"class": "nba-stat-table__overflow"})

        # Get table headers and remove hidden headers
        headers = table.findAll('th')
        header_all = [header.text.strip() for header in headers[1:]]
        header_list = [header for header in header_all if 'RANK' not in header][:-5]

        # Get table data
        rows = table.findAll('tr')[1:]
        player_stats = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]

        dataframe = pd.DataFrame(player_stats[1:], columns=header_list)
        dataframe['POSS'] = dataframe['POSS'].str.replace(',', '', regex=True)

        return dataframe