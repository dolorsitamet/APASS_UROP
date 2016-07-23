import os
from os.path import isfile, join
import time

start_time = time.time()

directory_name = "/Users/katiedunn/desktop/APASS_UROP/Data"
directory2 = "/Users/katiedunn/desktop/APASS_UROP"

###list of all folders of data###
data = os.listdir(directory_name)
#print data

to_file = open(directory2 + "//MPchecker", 'w')

#reading each folder
for i in range(1, len(data)):
	files = [f for f in os.listdir(directory_name + "//%s" % data[i]) if isfile(
		join(directory_name + "//%s" % data[i], f))] #all the files from a given night
	#print files

	###Copy relevant contents of data to a new file###
	for j in range(1, len(files)):
		from_file = open(directory_name + "/%s/%s" % (data[i], files[j]))

		for k, line in enumerate(from_file):
			if k == 0:
				name = line.split()[1]
				to_file.write(name)
				to_file.write(" ")
			elif k == 3:
				date_time = line.split()[2]
				(date, times) = date_time.split("T")
				(year, month, day) = date.split("-")
				(hour, minute, second) = times.split(":")
				decimal_day = (int(hour)*60*60 + int(minute)*60 + int(second)) / 86400.0

				to_file.write(year)
				to_file.write(" ")
				to_file.write(month)
				to_file.write(" ")
				to_file.write(day)
				to_file.write(str(decimal_day)[1:4])
				to_file.write(" ")
			elif k == 12:
				RA = line.split()[1]
				to_file.write(RA[:-1])
				to_file.write(" ")
			elif k == 13:
				dec = line.split()[1]
				to_file.write(dec)
				to_file.write("\n")
			elif k > 13:
				break

		from_file.close()

to_file.close()

print("--- %s seconds ---" % (time.time() - start_time))
