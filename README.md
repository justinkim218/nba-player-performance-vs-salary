# NBA Player Performances vs. Player Salary Analysis

## Description

This program provides a data visualization of NBA player performances versus their current salary.

During the NBA off-season and before the NBA trade deadline, a constant topic of discussion is determining a player's value and warranted salary. 

NBA player values were judged using their _Player Impact Estimate(PIE)_ which is an advanced stats metric created by the NBA. PIE aims to gauge an individual player's contribution to their team.

This data visualization seeks to assist franchises to:
- _Estimate player salary_: Given a player's PIE, determine their value and salary relative to other players.  
- _Identify underpaid players_: Find outliers that are outperforming their salary and are underpaid. Teams should seek to acquire these players or raise their salaries.
- _Identify overpaid players_: Find outliers that are underperforming their salary and are overpaid. Teams should seek to remove these players or lower their salaries.


### Built With

- Python
- Selenium Webdriver
- Beautiful Soup
- Pandas
- Plotly

## Installation

To start, execute the _main.py_ file. 

This file will check to see if _nba-stats-salaries.csv_ and _nba_salary_vs_PIE_scatter.html_ exists. If not it will create the two files.


## Usage

Once main.py is executed and has created the necessary files. Open _nba_salary_vs_PIE_scatter.html_ to see the data visualization of NBA player performances vs player salaries.

![Scatter Plot Screenshot](nba_salary_vs_PIE_scatter.png?raw=true)


## License

This project is licensed under the MIT License - see the LICENSE.txt file for details






