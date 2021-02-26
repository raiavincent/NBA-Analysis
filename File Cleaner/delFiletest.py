import os
import sys

directory = (r'C:\Users\Vincent\Documents\GitHub\Basketball-Analysis\File Cleaner')

filesInDirectory = os.listdir(directory)

txtFiles = [file for file in filesInDirectory if file.endswith(".txt")]

for file in txtFiles:
	path_to_file = os.path.join(directory, file)
	os.remove(path_to_file)