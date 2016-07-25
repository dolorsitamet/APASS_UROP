import os
from os.path import isfile, join
import time

#add creatino of directory
#delete line of zeroes
#check tolerance levels

start_time = time.time()

ROOT_PATH = "/Users/katiedunn/desktop/APASS_UROP/"
DATA_PATH = ROOT_PATH + "Data/"
WRITE_PATH = ROOT_PATH + "writeFiles/Objects_3/"
MARGIN_ERROR = .0004

DATA_FOLDER_LIST = os.listdir(DATA_PATH)

#column 4 is magnitude
#column 3 is object number
#column 9 and 10 are RA and dec
#column 13 is ref ID

if '.DS_Store' in DATA_FOLDER_LIST:
	DATA_FOLDER_LIST.remove('.DS_Store')

def get_RA_dec(line):
    split = line.split()
    return (float(split[8]), float(split[9]))

def is_star(line):
    split = line.split()
    return float(split[12]) != 0.

def remove_zero(line):
	split = line.split()
	zeroless = ' '.join(split[:12])
	return zeroless + "\n"

def process_file_lines(fileLine, keepStars=False):
	if not keepStars:
		return [ (idx,) + get_RA_dec(line) for idx, line in enumerate(fileLine) if not is_star(line)]
	else:
		return [ (idx,) + get_RA_dec(line) for idx, line in enumerate(fileLine)]

def get_n_files(nFolder):
	def isValidFile(fileName):
		return isfile(fileName) and ".DS_Store" not in fileName

	nFolderPath = DATA_PATH + "%s/moddat/" % nFolder
	directoryListing = os.listdir(nFolderPath) 
	files = [f for f in directoryListing if isValidFile(join(nFolderPath, f))] 
	return files

def get_file_lines(nFolder, nFileName):
	openedFile = open(DATA_PATH + "%s/moddat/%s" % (nFolder, nFileName))
	fileLines = list(openedFile.readlines())
	return fileLines

def write_matching_lines(writeFile, myFiveFiles, fileNo, lineNo):
	writeFile.write(remove_zero(myFiveFiles[fileNo][lineNo]))


for nFolder in DATA_FOLDER_LIST:
	# Looping through each of the folders
	nFileNames = get_n_files(nFolder)

	for j in range(0, len(nFileNames), 5):
		# j = 0, 5, 10, ...; this line goes to every fifth file

		writeFile = open(WRITE_PATH + "%s_objects_3.txt" % nFileNames[j][:12], 'w')
		# katie is so cute!
		# you look a lot nicer now

		myFiveFiles = [get_file_lines(nFolder, nFileNames[j+i]) for i in range(5)]
		myFiveData = [process_file_lines(fileLine) for fileLine in myFiveFiles]
		mfd = myFiveData

		a_ra_dec = myFiveData[0]
		b_ra_dec = myFiveData[1]
		c_ra_dec = myFiveData[2]
		d_ra_dec = myFiveData[3]
		e_ra_dec = myFiveData[4]
	 	# [[lineNumber, RA, dec], [...]]

	 	lineNo = [None]*5
	 	RA = [None]*5
	 	dec = [None]*5

		for (lineNo[0], RA[0], dec[0]) in mfd[0]:
			for (lineNo[1], RA[1], dec[1]) in mfd[1]:

				if (abs(RA[1]-RA[0]) <= MARGIN_ERROR and abs(dec[1]-dec[0]) <= MARGIN_ERROR):
					for (lineNo[2], RA[2], dec[2]) in mfd[2]:

						if (abs(RA[2] - RA[0]) <= MARGIN_ERROR and abs(dec[2] - dec[0]) <= MARGIN_ERROR):
							for (lineNo[3], RA[3], dec[3]) in mfd[3]:

								if (abs(RA[3] - RA[0]) <= MARGIN_ERROR and abs(dec[3] - dec[0]) <= MARGIN_ERROR):
									for (lineNo[4], RA[4], dec[4]) in mfd[4]:

										if (abs(RA[4] - RA[0]) <= MARGIN_ERROR and abs(dec[4] - dec[0]) <= MARGIN_ERROR):
											for i in range(5):
												write_matching_lines(writeFile, myFiveFiles, i, lineNo[i])		
											writeFile.write("\n")

		writeFile.close()
		# a.close()
		# b.close()
		# c.close()
		# d.close()
		# e.close()

print("--- %s seconds ---" % (time.time() - start_time))


