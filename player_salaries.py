import requests
from bs4 import BeautifulSoup
import pandas as pd


class PlayerSalaries:
    def __init__(self):
        self.soup = self.get_html()
        self.dataframe = self.get_data(self.soup)

    def get_html(self):
        nba_salary_url = "https://hoopshype.com/salaries/players/"

        response = requests.get(nba_salary_url)
        source = response.text

        return BeautifulSoup(source, 'html.parser')

    def get_data(self, soup):
        table = soup.findAll('tr')
        table_data = [[row.text.strip() for row in table[i].findAll('td')[1:3]] for i in range(len(table))]

        dataframe = pd.DataFrame(table_data[1:], columns=['PLAYER', '2021/22 Salary'])

        dataframe['2021/22 Salary'] = dataframe['2021/22 Salary'].str.replace('$', '', regex=True)
        dataframe['2021/22 Salary'] = dataframe['2021/22 Salary'].str.replace(',', '', regex=True)
        dataframe['2021/22 Salary'] = dataframe['2021/22 Salary'].astype(float)

        return dataframe
