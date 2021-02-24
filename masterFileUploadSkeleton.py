from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
from datetime import date
import calendar
import os

# code below sets up everything necessary for upload

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

# get day of week for uploading to Sunday folder
my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]
weekday = weekday.lower()

# get the a string of the current date for choosing the right file
dateString = datetime.strftime(datetime.now(), '%Y_%m_%d')

# current month to find the right folder to upload to
currentMonth = datetime.now().strftime('%B')
currentMonth = currentMonth.lower()

# R2 file is just one folder, no months
findRelationship = 'folderID'

# strings of folder IDs for Sundays
sundayFolderTeam = 'folderID'
sundayFolderPlayerSeason = 'folderID'
sundayFolderPlayerCareer = 'folderID'

# these next 3 if statements match the current month with the right folder ID
# DONE: wrap these all into one if statement, works fine but would be better
if currentMonth == 'january':
    monthFolderTeam = 'folderID'
    monthFolderPlayerSeason = 'folderID'
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'february':
    monthFolderTeam = 'folderID'
    monthFolderPlayerSeason = 'folderID'
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'march':
    monthFolderTeam = 'folderID'
    monthFolderPlayerSeason = 'folderID'
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'april':
    monthFolderTeam = 'folderID'
    monthFolderPlayerSeason = 'folderID'
    monthFolderPlayerCareer = 'folderID'
elif currentMonth == 'may':
    monthFolderTeam = 'folderID'
    monthFolderPlayerSeason = 'folderID'
    monthFolderPlayerCareer = 'folderID'

# using the os module to change the directory for the right file
os.chdir(r'path')
# use the dateString to find the day's file
todayFileFindRelationship = (f'R2 Measurements {dateString}.csv')
todayFileTeamStats = (f'Team Stats {dateString}.csv')

# upload file to the correct folder
findRelationshipFile = drive.CreateFile({'parents': [{'id': findRelationship}]})
findRelationshipFile.SetContentFile(todayFileFindRelationship)
findRelationshipFile.Upload()

teamStatsFile = drive.CreateFile({'parents': [{'id': monthFolderTeam}]})
teamStatsFile.SetContentFile(todayFileTeamStats)
teamStatsFile.Upload()

# using the os module to change the directory for the right file
os.chdir(r'path')
# use the dateString to find the day's file
todayFilePlayerSeasonStats = (f'2021 Season Stats as of {dateString}.csv')

playerSeasonStatsFile = drive.CreateFile({'parents': [{'id': monthFolderPlayerSeason}]})
playerSeasonStatsFile.SetContentFile(todayFilePlayerSeasonStats)
playerSeasonStatsFile.Upload()

# using the os module to change the directory for the right file
os.chdir(r'path')
# use the dateString to find the day's file
todayFilePlayerCareer = (f'Active Player Career Stats as of {dateString}.csv')

# upload file to the correct folder
todayPlayerCareerStats = drive.CreateFile({'parents': [{'id': monthFolderPlayerCareer}]})
todayPlayerCareerStats.SetContentFile(todayFilePlayerCareer)
todayPlayerCareerStats.Upload()

# if day is sunday, upload to the sunday files, same code as directly aboce, 
# but for Sunday files
if weekday == 'sunday':
    os.chdir(r'path')
    todayFileTeamStats = (f'Team Stats {dateString}.csv')
    
    teamStatsFile = drive.CreateFile({'parents': [{'id': sundayFolderTeam}]})
    teamStatsFile.SetContentFile(todayFileTeamStats)
    teamStatsFile.Upload()
    
    os.chdir(r'path')
    todayFilePlayerSeasonStats = (f'2021 Season Stats as of {dateString}.csv')
    
    playerSeasonStatsFile = drive.CreateFile({'parents': [{'id': sundayFolderPlayerSeason}]})
    playerSeasonStatsFile.SetContentFile(todayFilePlayerSeasonStats)
    playerSeasonStatsFile.Upload()
    
    os.chdir(r'path')
    todayFilePlayerCareer = (f'Active Player Career Stats as of {dateString}.csv')
    
    todayPlayerCareerStats = drive.CreateFile({'parents': [{'id': sundayFolderPlayerCareer}]})
    todayPlayerCareerStats.SetContentFile(todayFilePlayerCareer)
    todayPlayerCareerStats.Upload()
    
else:
    print('It is not Sunday.')
        
