import requests
from bs4 import BeautifulSoup
import pandas as pd


class TeamPayroll:
    def __init__(self):
        self.soup = self.get_html()
        self.dataframe = self.get_data(self.soup)

    def get_html(self):
        team_payroll_url = "https://hoopshype.com/salaries/"

        response = requests.get(team_payroll_url)
        source = response.text

        return BeautifulSoup(source, 'html.parser')

    def get_data(self, soup):
        table = soup.findAll('tr')
        table_data = [[row.text.strip() for row in table[i].findAll('td')[1:3]] for i in range(len(table))]

        dataframe = pd.DataFrame(table_data[1:], columns=['TEAM', 'Team Payroll'])

        dataframe['Team Payroll'] = dataframe['Team Payroll'].str.replace('$', '', regex=True)
        dataframe['Team Payroll'] = dataframe['Team Payroll'].str.replace(',', '', regex=True)
        dataframe["Team Payroll"] = dataframe["Team Payroll"].astype(float)
        dataframe['TEAM'] = [self.abbreviate_team(team_name) for team_name in dataframe['TEAM']]

        return dataframe

    def abbreviate_team(self, team_name):
        abbreviations = {
            "Atlanta": "ATL",
            "Brooklyn": "BKN",
            "Boston": "BOS",
            "Charlotte": "CHA",
            "Chicago": "CHI",
            "Cleveland": "CLE",
            "Dallas": "DAL",
            "Denver": "DEN",
            "Detroit": "DET",
            "Golden State": "GSW",
            "Houston": "HOU",
            "Indiana": "IND",
            "LA Clippers": "LAC",
            "LA Lakers": "LAL",
            "Memphis": "MEM",
            "Miami": "MIA",
            "Milwaukee": "MIL",
            "Minnesota": "MIN",
            "New Orleans": "NOP",
            "New York": "NYK",
            "Oklahoma City": "OKC",
            "Orlando": "ORL",
            "Philadelphia": "PHI",
            "Phoenix": "PHX",
            "Portland": "POR",
            "Sacramento": "SAC",
            "San Antonio": "SAS",
            "Toronto": "TOR",
            "Utah": "UTA",
            "Washington": "WAS",
        }

        return abbreviations[team_name]
