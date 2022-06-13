import pandas as pd
from player_stats import PlayerStats
from player_salaries import PlayerSalaries
from team_payroll import TeamPayroll
import plotly.express as px
import os.path


def create_csv():
    player_stats = PlayerStats().dataframe
    player_salaries = PlayerSalaries().dataframe
    team_payroll = TeamPayroll().dataframe

    merged_df = pd.merge(pd.merge(player_stats, player_salaries, on='PLAYER'), team_payroll, on="TEAM")
    merged_df["Percentage of Team Payroll"] = round(merged_df["2021/22 Salary"] / merged_df["Team Payroll"] * 100, 1)

    merged_df.to_csv('nba-stats-salaries.csv', index=False)


def create_scatter():
    df = pd.read_csv("nba-stats-salaries.csv")

    fig = px.scatter(
        df,
        x="PIE",
        y="2021/22 Salary",
        title="NBA Player Salaries vs. PIE"
              "<br><sub>Filtered for players with >500 possessions and >15 games played</sub>",
        size="Percentage of Team Payroll",
        hover_name="PLAYER",
        color="2021/22 Salary",
        color_continuous_scale="turbo",
    )

    fig.update_layout(
        xaxis_title="Player Impact Estimate (PIE)",
        yaxis_title="2021-2022 Salary",
        yaxis_range=[0, 50000000],
    )

    fig.write_html('nba_salary_vs_PIE_scatter.html')


if not os.path.isfile('nba-stats-salaries.csv'):
    create_csv()

if not os.path.isfile('nba_salary_vs_PIE_scatter.html'):
    create_scatter()
