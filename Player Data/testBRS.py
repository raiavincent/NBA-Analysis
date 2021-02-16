# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:14:22 2021

@author: Vincent
"""

from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
import pandas as pd

name = 'Lebron James'
team = 'NYK'
season = '2021'

roster = get_roster(team, season)

print(roster)

roster_df = pd.DataFrame(data=roster)