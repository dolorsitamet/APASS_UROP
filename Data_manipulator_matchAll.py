import os
from os.path import isfile, join
import time

#column 5 is magnitude
#column 7 is FWHM
#column 4 is object number
#column 10 and 11 are RA and dec
#column 14 is ref ID
#(1-indexed)

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
	relevantFieldFiles = elements[numberOfFilters+1:len(elements)]
	return (numberOfFilters, relevantFieldFiles)

def get_RA_dec(line):
    split = line.split()
    return [float(split[9]), float(split[10])]

def is_star(line):
    split = line.split()
    return float(split[13]) != 0.

def remove_zero(line):
	split = line.split()
	zeroless = ' '.join(split[:13])
	return zeroless + "\n"

def get_file_lines(nFolder, nFileName):
	openedFile = open(DATA_PATH + "%s/moddat/%s" % (nFolder, nFileName))
	fileLines = list(openedFile.readlines())
	return fileLines

def process_file_lines(fileLine, keepStars=False): #returns all line #s, RAs & decs for a file
	allFileLines = [ (idx,) + get_RA_dec(line) for idx, line in enumerate(fileLine) if not is_star(line)]
	if keepStars:
		allFileLines = [ (idx,) + get_RA_dec(line) for idx, line in enumerate(fileLine)]
	allFileLines = sorted(allFileLines, key=lambda x: x[1]) # sorts by RA
	return allFileLines

def same_point(RA, dec, i, j):
	return abs(RA[i]-RA[j]) <= MARGIN_ERROR and abs(dec[i]-dec[j]) <= MARGIN_ERROR


START_TIME = time.time()

ROOT_PATH = "/Users/katiedunn/desktop/APASS_UROP/"
DATA_PATH = ROOT_PATH + "Data/"
FLIST_PATH = ROOT_PATH + "flists/"

DATA_FOLDER_LIST = os.listdir(DATA_PATH)
if '.DS_Store' in DATA_FOLDER_LIST:
	DATA_FOLDER_LIST.remove('.DS_Store')

MARGIN_ERROR = .0007

#print DATA_FOLDER_LIST #['n140101', 'n140102', 'n140103', 'n140104', 'n140107', 'n140109', 'n140112', 'n140113', 'n140114', 'n140115', 'n140116', 'n140301', 'n140304', 'n140305', 'n140306', 'n140308', 'n140323', 'n140325', 'n140327', 'n140329', 'n140330', 'n140406', 'n140407', 'n140408', 'n140418', 'n140430', 'n140504', 's120809', 's120810', 's120811', 's120812', 's120813', 's120819', 's120820', 's120821', 's120826', 's120827', 's120828', 's120829', 's120830']
#print FLIST_FOLDER_LIST #['n140101', 'n140102', 'n140103', 'n140104', 'n140107', 'n140109', 'n140112', 'n140113', 'n140114', 'n140115', 'n140116', 'n140301', 'n140304', 'n140305', 'n140306', 'n140308', 'n140323', 'n140325', 'n140327', 'n140329', 'n140330', 'n140406', 'n140407', 'n140408', 'n140418', 'n140430', 'n140504', 's120809', 's120810', 's120811', 's120812', 's120813', 's120819', 's120820', 's120821', 's120826', 's120827', 's120828', 's120829', 's120830']

for nFolder in DATA_FOLDER_LIST:
	# Looping through each of the folders
	nFileNames = get_files(nFolder)
	flist = open(FLIST_PATH + "%s/FieldList" % nFolder)
	flistLines = list(flist.readlines())
	
	for field in flistLines:
		numberOfFilters, relevantFiles = process_flist_lines(field)

		if numberOfFilters > 2:

			myFiles = [get_file_lines(nFolder, relevantFiles[i]+"_new.txt") for i in range(numberOfFilters)]
			myData = [process_file_lines(fileLine) for fileLine in myFiles]

			lineNo = [None]*numberOfFilters
			RA = [None]*numberOfFilters
			dec = [None]*numberOfFilters

			for (lineNo[0], RA[0], dec[0]) in myFiveData[0]:
				for (lineNo[1], RA[1], dec[1]) in myFiveData[1]:

					if same_point(RA, dec, 0, 1):
						for (lineNo[2], RA[2], dec[2]) in myFiveData[2]:

							if same_point(RA, dec, 0, 2):
								write_matching_lines(writeFile, myFiveFiles, 0, lineNo[0]) 
								write_matching_lines(writeFile, myFiveFiles, 1, lineNo[1])
								write_matching_lines(writeFile, myFiveFiles, 2, lineNo[2])
								
								if numberOfFilters > 3:
									for (lineNo[3], RA[3], dec[3]) in myFiveData[3]:
										if same_point(RA, dec, 0, 3):
											write_matching_lines(writeFile, myFiveFiles, 3, lineNo[3])

											if numberOfFilters > 4:
												for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:
													if same_point(RA, dec, 0, 4):
														write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4])	
														writeFile.write("\n")


print("--- %s seconds ---" % (time.time() - START_TIME))