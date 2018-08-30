#Replace specific strings in a file with new string.
fd = open('make.mk', 'r')
tempstr = fd.read()
fd.close()
#to replace the file content don't open in append mode, write
#  mode start with the first character location
fd = open('make.mk', 'w')
tempstr = tempstr.replace('long', 'long123')
fd.write(tempstr)
fd.close()
