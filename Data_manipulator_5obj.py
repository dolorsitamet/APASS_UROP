import os
from os.path import isfile, join
import time

#add creatino of directory
#delete line of zeroes
#check tolerance levels

start_time = time.time()

directory_name = "/Users/katiedunn/desktop/APASS_UROP/Data"
data = os.listdir(directory_name)
margin_error = .0004

#column 5 is magnitude
#column 4 is object number
#column 10 and 11 are RA and dec
#column 14 is ref ID

if '.DS_Store' in data:
	data.remove('.DS_Store')

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

for i in range(0, len(data)):
	files = [f for f in os.listdir(directory_name + "/%s/moddat" % data[i]) if isfile(
		join(directory_name + "/%s/moddat" % data[i], f))] #all the files from a given night
	if '.DS_Store' in files:
		files.remove('.DS_Store')

	for j in range(0, len(files), 5):
		to_file = open("/Users/katiedunn/desktop/APASS_UROP/writeFiles/Objects_5/%s_objects.txt" % files[j][:12], 'w')

		print "New set of files " + str(time.time())
		a = open(directory_name + "/%s/moddat/%s" % (data[i], files[j]))
		b = open(directory_name + "/%s/moddat/%s" % (data[i], files[j+1]))
		c = open(directory_name + "/%s/moddat/%s" % (data[i], files[j+2]))
		d = open(directory_name + "/%s/moddat/%s" % (data[i], files[j+3]))
		e = open(directory_name + "/%s/moddat/%s" % (data[i], files[j+4]))

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

										if (abs(RA5 - RA1) <= margin_error and abs(dec5 - dec1) <= margin_error):
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

		#elif there are four files
		#elif there are three files
		#elif there are two files
		#else: ???

print("--- %s seconds ---" % (time.time() - start_time))