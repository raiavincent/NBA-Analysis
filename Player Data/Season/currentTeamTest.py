# current team testing, make a dict of the players and their team and
# then make into a dataframe

from sportsipy.nba.teams import Teams
from sportsipy.nba.teams import Team
from sportsipy.nba.roster import Player
from sportsipy.nba.roster import Roster
from basketball_reference_scraper.teams import get_roster
import pandas as pd

teams = Teams(year='2021')

abbr_list = []
for team in teams:
   abbr_list.append(team.abbreviation)

nameTeamDf = pd.DataFrame()

# DONE: The below worked
# need to make this so that i can add a column that is the abbr for team
# might have to init one datafram that adds to another, adding abbr 
# col that is abbr

for abbr in abbr_list:
    nextTeamDf = pd.DataFrame(data=get_roster(abbr,'2021'))
    nextTeamDf['Team'] = abbr
    nameTeamDf = nameTeamDf.append(nextTeamDf)
    