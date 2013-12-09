from sys import argv
from os.path import exists

# script, from_file, to_file = argv

# print "Copying form %s to %s" % (from_file,to_file)

# do on 1 line?
# in_file = open(from_file)
# indata = open(from_file).read()

# print "The inpur file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done"

# out_file.close()
# in_file.close()

# 1 line version
out_file = open("new_file.txt", 'w').write(open("test.txt").read())
# No need for the line below as Python automatically close the file after runnign the line above
# out_file.close()