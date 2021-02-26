import os
import sys

os.chdir(r'/home/pi/Documents/Basketball-Analysis/File Cleaner')

# Create a list of directories to clean
listOfDirectories = [r'/home/pi/Documents/Basketball-Analysis',
                    r'/home/pi/Documents/Basketball-Analysis/Player Data',
                    r'/home/pi/Documents/Basketball-Analysis/Player Data/Career',
                    r'/home/pi/Documents/Basketball-Analysis/Player Data/Season',
                    r'/home/pi/Documents/Basketball-Analysis/Excel Sheets']

for directory in listOfDirectories:
    # Get a list of each file in the directories
    allFiles = []
    filesInDirectory = os.listdir(directory)
    allFiles.append(filesInDirectory)
    # Get a list of the files of a certain type (csv) to be deleted
    csvFiles = [file for file in filesInDirectory if file.endswith(".csv")]
    # for the files in csvFiles, add name to the directory and delete that path
    for file in csvFiles:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)
