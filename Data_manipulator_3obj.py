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
directoryFiles = os.listdir(DATA_PATH)
MARGIN_ERROR = .0004


#column 4 is magnitude
#column 3 is object number
#column 9 and 10 are RA and dec
#column 13 is ref ID

if '.DS_Store' in directoryFiles:
	directoryFiles.remove('.DS_Store')

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

def get_ID_RA_Dec():
	pass

def is_valid_folder_names():
	pass


for dirFile in directoryFiles:
	# Looping through each of the folders
	myFiles = [1,1,1,1,1]

	files = [f for f in os.listdir(DATA_PATH + "%s/moddat" % dirFile) if isfile(
		join(DATA_PATH + "%s/moddat" % dirFile, f))] #all the files from a given night
	if '.DS_Store' in files:
		files.remove('.DS_Store')

	for j in range(0, len(files), 5):
		to_file = open(WRITE_PATH + "%s_objects_3.txt" % files[j][:12], 'w')

		a = open(DATA_PATH + "%s/moddat/%s" % (dirFile, files[j]))
		b = open(DATA_PATH + "%s/moddat/%s" % (dirFile, files[j+1]))
		c = open(DATA_PATH + "%s/moddat/%s" % (dirFile, files[j+2]))
		d = open(DATA_PATH + "%s/moddat/%s" % (dirFile, files[j+3]))
		e = open(DATA_PATH + "%s/moddat/%s" % (dirFile, files[j+4]))

		a_lines = list(a.readlines())
		b_lines = list(b.readlines())
		c_lines = list(c.readlines())
		d_lines = list(d.readlines())
		e_lines = list(e.readlines())

		a_ra_dec = process_file_lines(a_lines)
		b_ra_dec = process_file_lines(b_lines)
		c_ra_dec = process_file_lines(c_lines)
		d_ra_dec = process_file_lines(d_lines)
		e_ra_dec = process_file_lines(e_lines)
	 	# [[lineNumber, RA, dec], [...]]

		for idx1, RA1, dec1 in a_ra_dec:
			for idx2, RA2, dec2 in b_ra_dec:

				if (abs(RA2-RA1) <= MARGIN_ERROR and abs(dec2-dec1) <= MARGIN_ERROR):
					for idx3, RA3, dec3 in c_ra_dec:

						if (abs(RA3 - RA1) <= MARGIN_ERROR and abs(dec3 - dec1) <= MARGIN_ERROR):
							for idx4, RA4, dec4 in d_ra_dec:

								if (abs(RA4 - RA1) <= MARGIN_ERROR and abs(dec4 - dec1) <= MARGIN_ERROR):
									for idx5, RA5, dec5 in e_ra_dec:

										if (abs(RA5 - RA1) <= MARGIN_ERROR and abs(dec5 - dec1) <= MARGIN_ERROR):
											to_file.write(remove_zero(a_lines[idx1]))
											to_file.write(remove_zero(b_lines[idx2]))
											to_file.write(remove_zero(c_lines[idx3]))
											to_file.write(remove_zero(d_lines[idx4]))
											to_file.write(remove_zero(e_lines[idx5]))		
											to_file.write("\n")
		to_file.close()
		a.close()
		b.close()
		c.close()
		d.close()
		e.close()

print("--- %s seconds ---" % (time.time() - start_time))


