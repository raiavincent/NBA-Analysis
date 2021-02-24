from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
from datetime import date
import calendar
import os

gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Authenticate if they're not there

    # This is what solved the issues:
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})

    gauth.LocalWebserverAuth()

elif gauth.access_token_expired:

    # Refresh them if expired

    gauth.Refresh()
else:

    # Initialize the saved creds

    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")  

drive = GoogleDrive(gauth)

my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]
weekday = weekday.lower()

dateString = datetime.strftime(datetime.now(), '%Y_%m_%d')

currentMonth = datetime.now().strftime('%B')
currentMonth = currentMonth.lower()

findRelationship = 'folderID'

sundayFolderTeam = 'folderID'

sundayFolderPlayerSeason = 'folderID'

sundayFolderPlayerCareer = 'folderID'

if currentMonth == 'january':
    monthFolderTeam = 'folderID'
elif currentMonth == 'february':
    monthFolderTeam = 'folderID-'
elif currentMonth == 'march':
    monthFolderTeam = 'folderID'
elif currentMonth == 'april':
    monthFolderTeam = 'folderID'
elif currentMonth == 'may':
    monthFolderTeam = 'folderID'
    
if currentMonth == 'january':
    monthFolderPlayerSeason = 'folderID'
elif currentMonth == 'february':
    monthFolderPlayerSeason = 'folderID'
elif currentMonth == 'march':
    monthFolderPlayerSeason = 'folderID'
elif currentMonth == 'april':
    monthFolderPlayerSeason = 'folderID'
elif currentMonth == 'may':
    monthFolderPlayerSeason = 'folderID'
    
if currentMonth == 'january':
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'february':
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'march':
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'april':
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'may':
    monthFolderPlayerCareer = 'folderID'

os.chdir(r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\Excel Sheets')
todayFileFindRelationship = (f'R2 Measurements {dateString}.csv')
todayFileTeamStats = (f'Team Stats {dateString}.csv')

findRelationshipFile = drive.CreateFile({'parents': [{'id': findRelationship}]})
findRelationshipFile.SetContentFile(todayFileFindRelationship)
findRelationshipFile.Upload()

teamStatsFile = drive.CreateFile({'parents': [{'id': monthFolderTeam}]})
teamStatsFile.SetContentFile(todayFileTeamStats)
teamStatsFile.Upload()

os.chdir(r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\Player Data\Season')
todayFilePlayerSeasonStats = (f'2021 Season Stats as of {dateString}.csv')

playerSeasonStatsFile = drive.CreateFile({'parents': [{'id': monthFolderPlayerSeason}]})
playerSeasonStatsFile.SetContentFile(todayFilePlayerSeasonStats)
playerSeasonStatsFile.Upload()

os.chdir(r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\Player Data\Career')
todayFilePlayerCareer = (f'Active Player Career Stats as of {dateString}.csv')

todayPlayerCareerStats = drive.CreateFile({'parents': [{'id': monthFolderPlayerCareer}]})
todayPlayerCareerStats.SetContentFile(todayFilePlayerCareer)
todayPlayerCareerStats.Upload()

if weekday == 'sunday':
    os.chdir(r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\Excel Sheets')
    todayFileTeamStats = (f'Team Stats {dateString}.csv')
    
    teamStatsFile = drive.CreateFile({'parents': [{'id': sundayFolderTeam}]})
    teamStatsFile.SetContentFile(todayFileTeamStats)
    teamStatsFile.Upload()
    
    os.chdir(r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\Player Data\Season')
    todayFilePlayerSeasonStats = (f'2021 Season Stats as of {dateString}.csv')
    
    playerSeasonStatsFile = drive.CreateFile({'parents': [{'id': sundayFolderPlayerSeason}]})
    playerSeasonStatsFile.SetContentFile(todayFilePlayerSeasonStats)
    playerSeasonStatsFile.Upload()
    
    os.chdir(r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\Player Data\Career')
    todayFilePlayerCareer = (f'Active Player Career Stats as of {dateString}.csv')
    
    todayPlayerCareerStats = drive.CreateFile({'parents': [{'id': sundayFolderPlayerCareer}]})
    todayPlayerCareerStats.SetContentFile(todayFilePlayerCareer)
    todayPlayerCareerStats.Upload()
    
else:
    print('It is not sunday.')
        
