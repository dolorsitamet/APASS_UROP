import os
from os.path import isfile, join
import time

START_TIME = time.time()

ROOT_PATH = "/Users/katiedunn/desktop/APASS_UROP/"
DATA_PATH = ROOT_PATH + "Data/"
FLIST_PATH = ROOT_PATH + "flists/"

DATA_FOLDER_LIST = os.listdir(DATA_PATH)

#column 5 is magnitude
#column 7 is FWHM
#column 4 is object number
#column 10 and 11 are RA and dec
#column 14 is ref ID
##these are all 1-indexed

if '.DS_Store' in DATA_FOLDER_LIST:
	DATA_FOLDER_LIST.remove('.DS_Store')

def get_files(folder):
	def isValidFile(fileName):
		return isfile(fileName) and ".DS_Store" not in fileName

	nFolderPath = DATA_PATH + "%s/moddat/" % folder
	directoryListing = os.listdir(nFolderPath) 
	files = [f for f in directoryListing if isValidFile(join(nFolderPath, f))] 
	return files

def get_file_lines(nFolder, nFileName):
	openedFile = open(DATA_PATH + "%s/moddat/%s" % (nFolder, nFileName))
	fileLines = list(openedFile.readlines())
	return fileLines

def process_flist_lines(line):
	elements = line.split()
	numberOfFilters = (len(elements)-1)/2
	relevantFiles = elements[numberOfFilters+1:len(elements)]
	return (numberOfFilters, relevantFiles)

#print DATA_FOLDER_LIST #['n140101', 'n140102', 'n140103', 'n140104', 'n140107', 'n140109', 'n140112', 'n140113', 'n140114', 'n140115', 'n140116', 'n140301', 'n140304', 'n140305', 'n140306', 'n140308', 'n140323', 'n140325', 'n140327', 'n140329', 'n140330', 'n140406', 'n140407', 'n140408', 'n140418', 'n140430', 'n140504', 's120809', 's120810', 's120811', 's120812', 's120813', 's120819', 's120820', 's120821', 's120826', 's120827', 's120828', 's120829', 's120830']
#print FLIST_FOLDER_LIST #['n140101', 'n140102', 'n140103', 'n140104', 'n140107', 'n140109', 'n140112', 'n140113', 'n140114', 'n140115', 'n140116', 'n140301', 'n140304', 'n140305', 'n140306', 'n140308', 'n140323', 'n140325', 'n140327', 'n140329', 'n140330', 'n140406', 'n140407', 'n140408', 'n140418', 'n140430', 'n140504', 's120809', 's120810', 's120811', 's120812', 's120813', 's120819', 's120820', 's120821', 's120826', 's120827', 's120828', 's120829', 's120830']

for nFolder in DATA_FOLDER_LIST:
	# Looping through each of the folders
	nFileNames = get_files(nFolder)
	flist = open(FLIST_PATH + "%s/FieldList" % nFolder)
	flistLines = list(flist.readlines())
	for field in flistLines:
		numberOfFilters, relevantFiles = process_flist_lines(field)
		# if numberOfFilters == 5:

		# elif numberOfFilters == 4:

		# elif numberOfFitlers == 3:

		# elif numberOfFilters == 2:

		# else:


print("--- %s seconds ---" % (time.time() - START_TIME))
