import os
from os.path import isfile, join
import time


start_time = time.time()

ROOT_PATH = "/Users/katiedunn/desktop/APASS_UROP/"
DATA_PATH = ROOT_PATH + "Data/"
WRITE_PATH = ROOT_PATH + "writeFiles/Objects_3/"
MARGIN_ERROR = .0004 #may need to adjust this later

DATA_FOLDER_LIST = os.listdir(DATA_PATH)

#column 5 is magnitude
#column 4 is object number
#column 10 and 11 are RA and dec
#column 14 is ref ID

if '.DS_Store' in DATA_FOLDER_LIST:
	DATA_FOLDER_LIST.remove('.DS_Store')

def get_RA_dec(line):
    split = line.split()
    return (float(split[9]), float(split[10]))

def is_star(line):
    split = line.split()
    return float(split[13]) != 0.

def remove_zero(line):
	split = line.split()
	zeroless = ' '.join(split[:13])
	return zeroless + "\n"

def process_file_lines(fileLine, keepStars=False): #returns all line #s, RAs & decs for a file
	allFileLines = [ (idx,) + get_RA_dec(line) for idx, line in enumerate(fileLine) if not is_star(line)]
	if keepStars:
		allFileLines = [ (idx,) + get_RA_dec(line) for idx, line in enumerate(fileLine)]
	allFileLines = sorted(allFileLines, key=lambda x: x[1]) # sorts by RA
	return allFileLines

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

def pairwise_diff(array):
	n = len(array)
	nC2_tuples = [(i,j) for i in range(n) for j in range(n) if i<j]
	return [abs(array[i] - array[j]) for (i,j) in nC2_tuples]

def test_pairwise(diffArray):
	return all([d<MARGIN_ERROR for d in diffArray])

def same_point(RA, dec, i, j):
	return abs(RA[i]-RA[j]) <= MARGIN_ERROR and abs(dec[i]-dec[j]) <= MARGIN_ERROR

for nFolder in DATA_FOLDER_LIST:
	# Looping through each of the folders
	nFileNames = get_n_files(nFolder)

	for j in range(0, len(nFileNames), 5):
		print "New set of 5 files"
		# j = 0, 5, 10, ...; this line goes to every fifth file

		writeFile = open(WRITE_PATH + "%s_objects_3.txt" % nFileNames[j][:12], 'w')

		myFiveFiles = [get_file_lines(nFolder, nFileNames[j+i]) for i in range(5)]
		myFiveData = [process_file_lines(fileLine) for fileLine in myFiveFiles]

	 	lineNo = [None]*5
	 	RA = [None]*5
	 	dec = [None]*5

#01
		for (lineNo[0], RA[0], dec[0]) in myFiveData[0]:
			for (lineNo[1], RA[1], dec[1]) in myFiveData[1]:

				if same_point(RA, dec, 0, 1):
					for (lineNo[2], RA[2], dec[2]) in myFiveData[2]:

						if same_point(RA, dec, 0, 2):
							write_matching_lines(writeFile, myFiveFiles, 0, lineNo[0]) #012
							write_matching_lines(writeFile, myFiveFiles, 1, lineNo[1])
							write_matching_lines(writeFile, myFiveFiles, 2, lineNo[2])

							for (lineNo[3], RA[3], dec[3]) in myFiveData[3]:
								if same_point(RA, dec, 0, 3):
									write_matching_lines(writeFile, myFiveFiles, 3, lineNo[3]) #0123

									for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:
										if same_point(RA, dec, 0, 4):
											write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4]) #01234		
											writeFile.write("\n")
										else:
											writeFile.write("\n")
											#not working. don't want newline every time line4 doesn't match
								else:
									if same_point(RA, dec, 0, 4):
										write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4]) #0124
										writeFile.write("\n")
	
						else: 
							for (lineNo[3], RA[3], dec[3]) in myFiveData[3]:
								if same_point(RA, dec, 0, 3):
									write_matching_lines(writeFile, myFiveFiles, 3, lineNo[3]) #013

									for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:

										if same_point(RA, dec, 0, 4):
											write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4]) #0134		
											writeFile.write("\n")
										else:
											writeFile.write("\n")

#03
				else:
					for (lineNo[3], RA[3], dec[3]) in myFiveData[3]:

						if same_point(RA, dec, 0, 3):
							for (lineNo[2], RA[2], dec[2]) in myFiveData[2]:

								if same_point(RA, dec, 0, 2):
									write_matching_lines(writeFile, myFiveFiles, 0, lineNo[0]) #023
									write_matching_lines(writeFile, myFiveFiles, 2, lineNo[2])
									write_matching_lines(writeFile, myFiveFiles, 3, lineNo[3])
									for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:

										if same_point(RA, dec, 0, 4):
											write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4]) #0234
											writeFile.write("\n")
										else:
											writeFile.write("\n")
								else:
									for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:

										if same_point(RA, dec, 0, 4):
											write_matching_lines(writeFile, myFiveFiles, 0, lineNo[0]) #024
											write_matching_lines(writeFile, myFiveFiles, 2, lineNo[2])
											write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4])
											writeFile.write("\n")
#31		
		for (lineNo[3], RA[3], dec[3]) in myFiveData[3]:
			for (lineNo[1], RA[1], dec[1]) in myFiveData[1]:

				if same_point(RA, dec, 1, 3):
					for (lineNo[2], RA[2], dec[2]) in myFiveData[2]:

						if same_point(RA, dec, 2, 3):
							write_matching_lines(writeFile, myFiveFiles, 1, lineNo[1]) #123
							write_matching_lines(writeFile, myFiveFiles, 2, lineNo[2])
							write_matching_lines(writeFile, myFiveFiles, 3, lineNo[3])

							for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:

								if same_point(RA, dec, 0, 4):
									write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4]) #1234
									writeFile.write("\n")
								else:
									writeFile.write("\n")	
						else: 
							if same_point(RA, dec, 3, 4):
								write_matching_lines(writeFile, myFiveFiles, 1, lineNo[1]) #134
								write_matching_lines(writeFile, myFiveFiles, 3, lineNo[3])
								write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4])
								writeFile.write("\n")
#32
				else:
					for (lineNo[2], RA[2], dec[2]) in myFiveData[2]:
						if same_point(RA, dec, 2, 3):
							for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:
								write_matching_lines(writeFile, myFiveFiles, 0, lineNo[2]) #234
								write_matching_lines(writeFile, myFiveFiles, 2, lineNo[3])
								write_matching_lines(writeFile, myFiveFiles, 4, lineNo[4])
								writeFile.write("\n")				


 		writeFile.close()

print("--- %s seconds ---" % (time.time() - start_time))

# #01, 23, 04, 14

# 		for (lineNo[0], RA[0], dec[0]) in myFiveData[0]:
# 			for (lineNo[1], RA[1], dec[1]) in myFiveData[1]:

# 				if same_point(RA, dec, 0, 1):
# 					for (lineNo[2], RA[2], dec[2]) in myFiveData[2]:

# 						if (abs(RA[2] - RA[0]) <= MARGIN_ERROR and abs(dec[2] - dec[0]) <= MARGIN_ERROR):
# 							for (lineNo[3], RA[3], dec[3]) in myFiveData[3]:

# 								if (abs(RA[3] - RA[0]) <= MARGIN_ERROR and abs(dec[3] - dec[0]) <= MARGIN_ERROR):
# 									for (lineNo[4], RA[4], dec[4]) in myFiveData[4]:

# 										if (abs(RA[4] - RA[0]) <= MARGIN_ERROR and abs(dec[4] - dec[0]) <= MARGIN_ERROR):
# 											for i in range(5):
# 												write_matching_lines(writeFile, myFiveFiles, i, lineNo[i])		
# 											writeFile.write("\n")
# 			for 4:
# 				if same_point(RA, dec, 0, 4):
					
# 		for 1:
# 			for 4:
# 				if same_point(RA, dec, 1, 2):

# 		for 2:
# 			for 3:


# 					# Check if 2==3==4

# 		writeFile.close()
# 		# a.close()
# 		# b.close()
# 		# c.close()
# 		# d.close()
# 		# e.close()

# 		print("--- %s seconds ---" % (time.time() - start_time))


# for 0
# 	for 1
# 		if test(0,1)

# for 2
# 	for 3
# 		for 


