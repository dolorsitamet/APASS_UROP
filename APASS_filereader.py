import os
from os.path import isfile, join
import time

start_time = time.time()

directory_name = "/Users/katiedunn/desktop/APASS_UROP/Data"

###list of all folders of data###
data = os.listdir(directory_name)
if '.DS_Store' in data:
	data.remove('.DS_Store')

#reading each folder
for i in range(0, len(data)-1):
	files = [f for f in os.listdir(directory_name + "//%s" % data[i]) if isfile(
		join(directory_name + "//%s" % data[i], f))] #all the files from a given night
	if '.DS_Store' in files:
		files.remove('.DS_Store')
	if not os.path.exists(directory_name + "/%s/moddat" % data[i]):
	 	os.makedirs(directory_name + "/%s/moddat" % data[i])

	# ###Copy relevant contents of data to a new file###
	for j in range(1, len(files)):
		from_file = open(directory_name + "/%s/%s" % (data[i], files[j]))
		to_file = open(directory_name + "/%s/moddat/%s_new.txt" % (data[i], files[j]), 'w')
		#print "Copying relevant part of %s" % (files[j])
		
		for line in from_file.readlines():
  			if not('#' in line): #ie if not header
  				split_data = line.split()
  				split_data = ' '.join(split_data)
  				to_file.write(split_data)
  				to_file.write("\n")

	 	from_file.close()
		to_file.close()

print("--- %s seconds ---" % (time.time() - start_time))
