from sportsipy.nba.teams import Teams
from sportsipy.nba.teams import Team
import pandas as pd
from basketball_reference_scraper.teams import get_team_misc
from datetime import datetime
import schedule
import time
from variable import dataframe_order
import gspread
from nbaSecrets import nbaTeamFolderId, teamDashboardURL

print('Running createDF.py.')

def makeTeamDf():
    startTime = datetime.now()
    
    teams = Teams(year='2021')
    
    abbr_list = []
    for team in teams:
       abbr_list.append(team.abbreviation)
    
    league_df = pd.DataFrame()
    print('Gathering main statistics.')
    for abbr in abbr_list:
        nextTeam = Team(abbr)
        team_df = pd.DataFrame(data=nextTeam.dataframe)
        league_df = pd.concat([league_df,team_df])
    
    print('DONE: Gathered main statistics.')
    
    # DONE: get wins and loss to add to dataframe using basketball_reference_scraper
    print('Gathering misc statistics.')
    misc_data = pd.DataFrame()
    for abbr in abbr_list:
        nextMisc = get_team_misc(abbr,2021)
        misc_df = pd.DataFrame(data=nextMisc)
        misc_t = misc_df.transpose()
        misc_data = pd.concat([misc_data,misc_t]) 
    # this works but it got fucked up, use transpose?
    # need to compare colums as it wont concat with similar columns    
    # all good now
    print('DONE: Gathered misc statistics.')
    
    
    print('Sorting frames and adding necessary columns.')
    # set 'TEAM' as index for misc_data, as it has none
    misc_data = misc_data.set_index('TEAM')
    
    # sort the dataframes so that we have (hopefully) no errors when adding cols
    misc_data = misc_data.sort_values(['TEAM'])
    league_df = league_df.sort_values(['abbreviation'])
    
    # need to take necessary misc_data columns and add to league_df
    league_df['W'] = misc_data['W']
    league_df['L'] = misc_data['L']
    league_df['GP'] = league_df['W'] + league_df['L']
    print('DONE: Frames sorted and columns added.')
    
    # DONE: calculate EWP wins and losses for the whole season as well as games
    # played.
    
    # Pythagorean (Expected) Winning Percentage Formula=
    # (Points Scored)^16.5/[Points Scored)^16.5 + (Points Allowed)^16.5)]
    
    exponent = 16.5
    gamesInSeason = 82
    decimals = 0
    
    print('Calculating EWP.')
    
    league_df['EWP'] = round(((league_df['points']**exponent)/
    ((league_df['points']**exponent)+(league_df['opp_points']**exponent))),2)
    
    # DONE: Figure out how to round these.
    
    league_df['PW'] = league_df['GP'] * league_df['EWP']
    league_df['PW'] = league_df['PW'].apply(lambda x: round(x, decimals))
    league_df['PL'] = league_df['GP'] * (1-league_df['EWP'])
    league_df['PL'] = league_df['PL'].apply(lambda x: round(x, decimals))
    league_df['PW Season'] = gamesInSeason * league_df['EWP']
    league_df['PW Season'] = league_df['PW Season'].apply(lambda x: round(x, 
                                                                          decimals))
    league_df['PL Season'] = gamesInSeason * (1-league_df['EWP'])
    league_df['PL Season'] = league_df['PL Season'].apply(lambda x: round(x, 
                                                                          decimals))
    league_df['Ahead/Behind'] = league_df['W'] - league_df['PW']
    
    print('DONE: EWP calculated.')
    
    # Done: Add in differentials.
    
    print('Calculating differentials.')
    
    league_df['Point Diff'] = league_df['points'] - league_df['opp_points']
    league_df['Assist Diff'] = league_df['assists'] - league_df['opp_assists']
    league_df['Block Diff'] = league_df['blocks'] - league_df['opp_blocks']
    league_df['Def Reb Diff'] = (league_df['defensive_rebounds'] - 
                                         league_df['opp_defensive_rebounds'])
    league_df['FG Att Diff'] = (league_df['field_goal_attempts'] - 
                                        league_df['opp_field_goal_attempts'])
    league_df['FG Diff'] = (league_df['field_goals'] - 
                                    league_df['opp_field_goals'])
    league_df['FT Diff'] = league_df['free_throws'] - league_df['opp_free_throws']
    league_df['FT Att Diff'] = (league_df['free_throw_attempts'] - 
                                        league_df['opp_free_throw_attempts'])
    league_df['Off Reb Diff'] = (league_df['offensive_rebounds'] - 
                                         league_df['opp_offensive_rebounds'])
    league_df['Personal Foul Diff'] = (league_df['personal_fouls'] - 
                                       league_df['opp_personal_fouls'])
    league_df['Steal Diff'] = league_df['steals'] - league_df['opp_steals']
    league_df['3pt Att Diff'] = (league_df['three_point_field_goal_attempts'] - 
                                 league_df['opp_three_point_field_goal_attempts'])
    league_df['3pt FG Diff'] = (league_df['three_point_field_goals'] - 
                                league_df['opp_three_point_field_goals'])
    league_df['Rebound Diff'] = (league_df['total_rebounds'] - 
                                 league_df['opp_total_rebounds'])
    league_df['Turnover Diff'] = league_df['turnovers'] - league_df['opp_turnovers']
    league_df['2pt FG Att Diff'] = (league_df['two_point_field_goal_attempts'] - 
                                    league_df['opp_two_point_field_goal_attempts'])
    league_df['2pt FG Diff'] = (league_df['two_point_field_goals'] - 
                                    league_df['opp_two_point_field_goals'])
    league_df['abbreviation'].fillna('AVG', inplace = True)
    
    print('DONE: Calculated differentials.')
    
    # consider dropping rank from this list, as it is only based off points
    league_df = league_df[dataframe_order]
    
    league_df = league_df.sort_values(['EWP'],ascending=False)
    league_df = league_df.reset_index(drop=True)
    
    print('Dataframe created.')
    
    # gc authorizes and lets us access the spreadsheets
    gc = gspread.oauth()
    dateString = datetime.strftime(datetime.now(), '%Y_%m_%d')
    
    # create the workbook where the day's data will go
    # add in folder_id to place it in the folder we want
    sh = gc.create(f'NBA Team Data as of {dateString}',folder_id=nbaTeamFolderId)
    
    # access the first sheet of that newly created workbook
    worksheet = sh.get_worksheet(0)
    
    # edit the worksheet with the created dataframe for the day's data
    worksheet.update([league_df.columns.values.tolist()] + league_df.values.tolist())
    
    # open the main workbook with that workbook's url
    db = gc.open_by_url(teamDashboardURL)
    
    # changed this over to the second sheet so the dashboard can be the first sheet
    # dbws is the database worksheet, as in the main workbook that is updated and
    # used to analyze and pick from
    dbws = db.get_worksheet(1)
    
    # below clears the stock sheet so it can be overwritten with updates
    # z1000 is probably overkill but would rather over kill than underkill
    range_of_cells = dbws.range('A1:Z1000')
    for cell in range_of_cells:
        cell.value = ''
    dbws.update_cells(range_of_cells)
    
    # update the spreadsheet in the database workbook with the df
    dbws.update([league_df.columns.values.tolist()] + league_df.values.tolist())
    
    print('Sheets updated and created. Script complete.')
    
    print(datetime.now()-startTime)

schedule.every().day.at("05:00").do(makeTeamDf)

while True:
    schedule.run_pending()
    time.sleep(1)
