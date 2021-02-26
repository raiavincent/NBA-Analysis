import os
import sys

# so what I have here in a sense works, but it should be one larger for loop
# it is combining the wrong directories and files
# but its almost there, needs to be a larger loop that calls each directory

os.chdir(r'/home/pi/Documents/Basketball-Analysis/File Cleaner')

# Establish the text file with directories to be cleaned
directoryText = 'directories.txt'

# Create a list from that directory
listOfDirectories = [r'/home/pi/Documents/Basketball-Analysis',
                     r'/home/pi/Documents/Basketball-Analysis/Player Data',
                     r'/home/pi/Documents/Basketball-Analysis/Player Data/Career',
                     r'/home/pi/Documents/Basketball-Analysis/Player Data/Season',
                     r'/home/pi/Documents/Basketball-Analysis/Excel Sheets']

# Get a list of each file in the directories

allFiles = []

for directory in listOfDirectories:
    filesInDirectory = os.listdir(directory)
    allFiles.append(filesInDirectory)

# Get a list of the files of a certain type (csv) to be deleted
csvFiles = [file for file in filesInDirectory if file.endswith(".csv")]

for directory in listOfDirectories:
    csvFiles = [file for file in filesInDirectory if file.endswith(".csv")]
    for file in csvFiles:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)