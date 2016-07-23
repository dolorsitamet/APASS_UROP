import os
from os.path import isfile, join
import time

start_time = time.time()

directory_name = "/Users/katiedunn/desktop/APASS_UROP/Data/Objects"
files = os.listdir(directory_name)
if '.DS_Store' in files:
	files.remove('.DS_Store')
#column 4 is magnitude
#column 3 is object number
#column 9 and 10 are RA and dec
#column 13 is ref ID

for i in range(0, len(files)-1):
	from_file = open(directory_name + "/%s" % files[i])
	to_file = open(directory_name + "/Starless/%s_objects_starless.txt" % files[i], 'w')

	for line in from_file.readlines():
		if line == '\n':
			pass
  		else:
  			refID = line.split()[12]
  			if refID == "0": 
  				to_file.write(line)

#  	for line in to_file.readlines():

	from_file.close()
	to_file.close()

print("--- %s seconds ---" % (time.time() - start_time))
