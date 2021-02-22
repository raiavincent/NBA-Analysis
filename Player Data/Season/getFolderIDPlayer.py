# get the current month and pick folder ID from there
from datetime import datetime


sundayFolder = '1S819eQ1oB4eFded5y6G01BhTFtUWhAFe'
    
currentMonth = datetime.now().strftime('%B')
currentMonth = currentMonth.lower()
print(currentMonth)

if currentMonth == 'january':
    monthFolder = '1OJ8taJ-H4iSJltJ9P5w97vnXfN_644N8'
elif currentMonth == 'february':
    monthFolder = '1ySGmEz2HcRHNcQ3k1TWcTg9F9e3I2VYi'
elif currentMonth == 'march':
    monthFolder = '1V1gMH9ofsGL7KhIZNqltIwtZS3nUwKY0'
elif currentMonth == 'april':
    monthFolder = '1h2nfROI252VmcYSgyRIwtruixEeQhKQp'
elif currentMonth == 'may':
    monthFolder = '1vKvKFg8L6aPhEQQSM2iRSAWL7b0K9Skr'
    
    
print(monthFolder)

