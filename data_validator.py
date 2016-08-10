#in progress -- could just implement when 5th pairing is checked, also check fwhms, write new files.

import os
from os.path import isfile, join
import time

start_time = time.time()

ROOT_PATH = "/Users/katiedunn/desktop/APASS_UROP/"
DATA_PATH = ROOT_PATH + "Data/"
WRITE_PATH = ROOT_PATH + "writeFiles/Objects_3/"

DATA_FOLDER_LIST = os.listdir(DATA_PATH)

#column 5 is magnitude
#column 4 is object number
#column 10 and 11 are RA and dec
#column 14 is ref ID

if '.DS_Store' in DATA_FOLDER_LIST:
	DATA_FOLDER_LIST.remove('.DS_Store')

def get_n_files(nFolder):
	def isValidFile(fileName):
		return isfile(fileName) and ".DS_Store" not in fileName

	nFolderPath = DATA_PATH + "%s/moddat/" % nFolder
	directoryListing = os.listdir(nFolderPath) 
	files = [f for f in directoryListing if isValidFile(join(nFolderPath, f))] 
	return files

counter = 0 #see how many things are removed



print("--- %s seconds ---" % (time.time() - start_time))
