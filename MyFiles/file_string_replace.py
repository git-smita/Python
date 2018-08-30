#Replace specific strings in a file with new string.
fd = open('make.mk', 'r')
tempstr = fd.read()
fd.close()
# To replace the file content don't open in append mode, write

fd = open('make.mk', 'w')
tempstr = tempstr.replace('long', 'long123')
fd.write(tempstr)
fd.close()
