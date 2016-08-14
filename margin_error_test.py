
import os
from os.path import isfile, join
import time

#add creatino of directory
#delete line of zeroes
#check tolerance levels

start_time = time.time()

directory_name = "/Users/katiedunn/desktop/APASS_UROP/Data"
data = os.listdir(directory_name)
margin_error = .0001

#column 5 is magnitude
#column 4 is object number
#column 10 and 11 are RA and dec
#column 14 is ref ID

if '.DS_Store' in data:
	data.remove('.DS_Store')

def get_RA_dec(line):
	split = line.split()
	return [float(split[9]), float(split[10])]

def get_FWHM(line):
	split = line.split()
	FWHM = float(split[6])
	if FWHM > 2:
		return True
	else:
		return False

def is_star(line):
    split = line.split()
    return float(split[13]) != 0.

def remove_zero(line):
	split = line.split()
	zeroless = ' '.join(split[:13])
	return zeroless + "\n"

to_file = open("/Users/katiedunn/desktop/APASS_UROP/writeFiles/margin_error_test.txt", 'w')

for i in range(0, 1):  #len(data)):
	files = [f for f in os.listdir(directory_name + "/%s/moddat" % data[i]) if isfile(
		join(directory_name + "/%s/moddat" % data[i], f))] #all the files from a given night
	if '.DS_Store' in files:
		files.remove('.DS_Store')
	
	while margin_error < .005:

		counter = 0

		a = open(directory_name + "/%s/moddat/%s" % (data[i], files[5]))
		b = open(directory_name + "/%s/moddat/%s" % (data[i], files[6]))
		c = open(directory_name + "/%s/moddat/%s" % (data[i], files[7]))
		d = open(directory_name + "/%s/moddat/%s" % (data[i], files[8]))
		e = open(directory_name + "/%s/moddat/%s" % (data[i], files[9]))

		a_lines = list(a.readlines())
		b_lines = list(b.readlines())
		c_lines = list(c.readlines())
		d_lines = list(d.readlines())
		e_lines = list(e.readlines())

		a_ra_dec = [[idx] + get_RA_dec(line) for idx, line in enumerate(a_lines) if not is_star(line)]
		b_ra_dec = [[idx] + get_RA_dec(line) for idx, line in enumerate(b_lines) if not is_star(line)]
		c_ra_dec = [[idx] + get_RA_dec(line) for idx, line in enumerate(c_lines) if not is_star(line)]
		d_ra_dec = [[idx] + get_RA_dec(line) for idx, line in enumerate(d_lines) if not is_star(line)]
	 	e_ra_dec = [[idx] + get_RA_dec(line) for idx, line in enumerate(e_lines) if not is_star(line)]

		for idx1, RA1, dec1 in a_ra_dec:
			for idx2, RA2, dec2 in b_ra_dec:

				if (abs(RA2-RA1) <= margin_error and abs(dec2-dec1) <= margin_error):
					for idx3, RA3, dec3 in c_ra_dec:

						if (abs(RA3 - RA1) <= margin_error and abs(dec3 - dec1) <= margin_error):
							for idx4, RA4, dec4 in d_ra_dec:

								if (abs(RA4 - RA1) <= margin_error and abs(dec4 - dec1) <= margin_error):

									for idx5, RA5, dec5 in e_ra_dec:
										if (abs(RA5 - RA1) <= margin_error and abs(dec5 - dec1) <= margin_error) and get_FWHM(e_lines[idx5]):
											counter = counter + 1

		to_file.write(str(margin_error))
		to_file.write(" ")		
		to_file.write(str(counter))
		to_file.write("\n")
		margin_error = margin_error + 0.0001


to_file.close()
a.close()
b.close()
c.close()
d.close()
e.close()

print("--- %s seconds ---" % (time.time() - start_time))