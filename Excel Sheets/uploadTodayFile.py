from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
from config import folder

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

dateString = datetime.strftime(datetime.now(), '%Y_%m_%d')

todayFile = ('Team Stats ' + dateString + '.csv')
# TODO: the folder ID should be added from a config file
file = drive.CreateFile({'parents': [{'id': folder}]})
file.SetContentFile(todayFile)
file.Upload()
